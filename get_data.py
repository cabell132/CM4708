# A script for getting data from the Spotify & Beatport API.
from spotify import Spotify
from beatport.client import BeatportClient
from tqdm import tqdm
import urllib.request
import subprocess
import os
import json

class GetData(object):

    def __init__(self):
        self.spotify = Spotify()
        self.beatport = BeatportClient()
        self.sample_folder = 'samples'

    def adjust_file_name(self, file_name:str)->str:
        """Function to adjust the file name for windows.
        
        Args:
            file_name (str): the file name
            
        Returns:
            str: the adjusted file name
            
        """    

        invalid_chars = "\\/:*?\"<>|"
        adjusted_name = ""
        for char in file_name:
            if char in invalid_chars:
                adjusted_name += "_"
            else:
                adjusted_name += char
        return adjusted_name
    
    def get_enao_playlists(self)->list:
        """Function to get the playlists from the Every Noise At Once Spotify account.

        Returns:
            list: the playlists

        """

        return self.spotify.get_user_playlists(username="thesoundsofspotify")
    
    def get_playlist_isrcs(self)->dict:
        """Function to get a list ISRCS from a Every Noise At Once
            playlist and saves them to a file.

        """

        user_playlists = self.get_enao_playlists()

        p_bar = tqdm(user_playlists['items'], total=len(user_playlists['items']), desc='Playlists')
        for playlist in p_bar:
            # we are only intresred in the playlist if the playlist name starts with 'The Sound of'
            # but is not named 'The Sound of Everything' as these playlists are grouped by genre
            if playlist['name'].startswith('The Sound of') and playlist['name'] != 'The Sound of Everything':
                # parse the genre from the playlist name
                genre = playlist['name'].replace('The Sound of ', '')
                p_bar.set_description('Genre: {}'.format(genre))

                # create new folder for the genre samples
                folder = os.path.join(self.samples_folder,self.adjust_file_name(genre))
                
                # check if the folder exists
                if not os.path.exists(folder):
                    os.makedirs(folder)
                file = os.path.join(folder, 'isrc.json')
                if not os.path.exists(file):
                    # Get the playlist
                    playlist = self.spotify.get_playlist(playlist['id'])
                    # get the track isrcs from the playlist
                    with open(file, 'a') as json_file:
                        for track in playlist['tracks']['items']:
                            if track.get('track'):
                                if track['track'].get('external_ids'):
                                    if track['track'].get('external_ids').get('isrc'):
                                        json_file.write(f"{track['track']['external_ids'].get('isrc')}\n")

    def get_beatport_samples(self):
        """ 
            Function to get the samples urls from Beatport using the ISRCs list files and 
            saving to json.



        """

        # get the isrcs files from the samples folder
        for root, dirs, files in os.walk(self.sample_folder):
            for file in files:
                if file.endswith("isrc.json"):
                    # get the genre from the folder name
                    genre = root.replace('samples\\', '')
                    # get the isrcs from the file
                    with open(os.path.join(root, file), 'r') as isrc_file:
                        isrcs = isrc_file.readlines()
                        isrcs = [isrc.strip() for isrc in isrcs]
                    # break the track isrcs into chunks of 50 as the beatport api only allows the return 
                    # of 150 tracks per request and a isrc can be used to get multiple tracks
                    track_isrcs_chunks = [isrcs[i:i+50] for i in range(0, len(isrcs), 50)]

                    # iterate through the chunks
                    p_bar = tqdm(track_isrcs_chunks, total=len(track_isrcs_chunks), desc="Getting tracks from Beatport")
                    
                    samples = {}
                    # create file for the samples urls
                    samples_file = f'{self.sample_folder}/{self.adjust_file_name(genre)}/samples.json'
                    cnt = 0
                    if not os.path.exists(samples_file):
                        for chunk in p_bar:
                            cnt += len(chunk)
                            p_bar.set_description("Getting tracks from Beatport for playlist: {} tracks: {}".format(genre, cnt))
                            search_request = ",".join(chunk)
                            # get the tracks from the beatport api
                            beatport_tracks = self.beatport.catalog.tracks.search(isrc=search_request)['results']
                            # add the sample url to the samples dict with the isrc as the key
                            for beatport_track in beatport_tracks:
                                samples[beatport_track['isrc']] = beatport_track['sample_url']

                        # write the samples to the samples file
                        with open(samples_file, 'w') as json_file:
                            json_file.write(json.dumps(samples))

    def download_samples(self):
        """Function to download the samples from the samples urls json file.

        """
        # initiate melspectrogram converter
        subprocess.Popen(['python', 'convert_to_melspectrograms.py'])

        # get the samples files from the samples folder
        for root, dirs, files in os.walk(self.sample_folder):
            for file in files:
                if file.endswith("samples.json"):
                    # get the genre from the folder name
                    genre = root.replace('samples\\', '')
                    # get the isrcs from the file
                    # create new folder for the genre samples
                    folder = f'{self.sample_folder}/{genre}/mp3'
                    # check if the folder exists
                    if not os.path.exists(folder):
                        with open(os.path.join(root, file), 'r') as samples_file:
                            data = json.load(samples_file)
                            # iterate through the samples
                            os.makedirs(folder)
                            p_bar = tqdm(data.items(), total=len(data), desc="Downloading samples for {}".format(genre))
                            for isrc, sample_url in p_bar:
                                if sample_url:
                                    # get the file name from the sample url
                                    file_name = f"{isrc}.mp3"
                                    # create the file path
                                    file_path = os.path.join(root, file_name)
                                    # download the sample
                                    try:
                                        urllib.request.urlretrieve(sample_url, file_path)
                                    except urllib.request.HTTPError as e:
                                        print(e)
                                        continue

                                    p_bar.set_description("Downloading samples for {} file: {}".format(genre, file_name))
                                else:
                                    p_bar.set_description("Downloading samples for {} file: None".format(genre))

if __name__ == "__main__":
    # create the downloader
    get_data = GetData()
    # get the isrcs from the playlists
    get_data.get_playlist_isrcs()
    # get the samples urls from the isrcs
    get_data.get_beatport_samples()
    # download the samples
    get_data.download_samples()