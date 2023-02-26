from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import util
import spotipy
from tqdm import tqdm
import json
import os

class Spotify():

    def __init__(self):
        """ 
        Initialize the Spotify class by authenticating with the Spotify API
        
        """

        __creds = self.getCreds()
        SCOPE = 'user-library-read user-read-recently-played playlist-modify-public playlist-read-private playlist-modify-private' 
        auth_manager = SpotifyClientCredentials(client_id=__creds['client_id'], client_secret=__creds['client_secret'])

        self.client = spotipy.Spotify(auth_manager=auth_manager)

    def getCreds(self)->dict:
        """ 
        Function to get the credentials from the environment variables for increased security
        to avoid hardcoding the credentials in the code

        Returns:
            dict: the credentials
        """
        with open(os.environ['TOKENS_PATH'], 'r') as f:
            self.token_json = json.load(f)['spotify']

        return self.token_json

    # parse parms from next url
    def parse_params(self, url:str)->dict:
        """ 
        Function that parses the next url to get the page number and the search parameters
        
        Args:
            url (str): the next url
        
        Returns:
            dict: the page number and the search parameters
        """
        url = url.split('?')[1]
        url = url.split('&')
        params = {}
        for param in url:
            key, value = param.split('=')
            params[key] = value
        return params

    def get_playlist(self, playlist_id:str)->dict:
        """
        Function that gets the playlist from the Spotify API and iterates through the pages to get all the tracks
        given the playlist id

        Args:
            playlist_id (str): the playlist id

        Returns:
            dict: the playlist data
        """
        data = self.client.playlist(playlist_id)

        offsets = [i for i in range(100, data['tracks']['total'], 100)]
        p_bar = tqdm(offsets, total=len(offsets), desc="Getting playlist tracks")
        for offset in p_bar:
            p_bar.set_description("Getting playlist tracks for id: {} offset: {}".format(playlist_id, offset))
            result = self.client.playlist_tracks(data['id'], limit=100, offset=offset)
            
            for track in result['items']:
                    
                data['tracks']['items'].append(track)

        cnt = 1
        for track in data['tracks']['items']:
            track['track_no'] = cnt
            cnt += 1
        if data['tracks']['items']:
            data['last_updated'] = max([x['added_at'] for x in data['tracks']['items']])
        data['topic'] = "spotify_playlist_requests"
        return data

    def get_user_playlists(self, username:str)->dict:
        """
        Function that gets the user playlists from the Spotify API and iterates through the pages to get all the playlists
        given the username

        Args:
            username (str): the username

        Returns:
            dict: the user playlists data

        """
        data = self.client.user_playlists(username)
        offsets = [i for i in range(50, data['total'], 50)]
        p_bar = tqdm(offsets, total=len(offsets), desc="Getting user playlists")
        for offset in p_bar:
            p_bar.set_description("Getting user playlists for username: {} offset: {}".format(username, offset))
            result = self.client.user_playlists(username, limit=50, offset=offset)
            for playlist in result['items']:
                data['items'].append(playlist)
        return data


    def create_spotify_playlist(self, playlist_name:str, track_ids:list, public:bool = False)->tuple:
        """
        Function that creates a Spotify playlist given the playlist name and the track ids

        Args:
            playlist_name (str): the playlist name
            track_ids (list): the track ids
            public (bool, optional): whether the playlist is public or not. Defaults to False.

        Returns:
            tuple: the playlist id and the spotify url

        """

        __creds = self.getCreds()
        username=__creds['username']
        token = util.prompt_for_user_token(username=__creds['username'], scope=__creds['scope'], client_id=__creds['client_id'], client_secret=__creds['client_secret'], redirect_uri=__creds['redirect_uri'])



        spotify = spotipy.Spotify(auth=token)



        user_playlists = {}
        playlists = spotify.user_playlists(username,limit=50,offset=0)
        j = 0
        while 50*j < playlists['total']:
            playlists = spotify.user_playlists(username,limit=50,offset=50*j)
            for playlist in playlists['items']:
                if playlist['owner']['id'] == username:
                    user_playlists[playlist['name']] = [playlist['id'], playlist['external_urls']['spotify']]
            j += 1
        
        if playlist_name in list(user_playlists.keys()):
            playlist_id, spotify_url = user_playlists[playlist_name]

        else:
            res = spotify.user_playlist_create(username, name = playlist_name, public=public)
            playlist_id = res['id']
            spotify_url = res['external_urls']['spotify']
            print("{} Added!".format(playlist_name))

        for i in range(round((len(track_ids)+50)/100)):
            if token:
                results = spotify.user_playlist_add_tracks(username, playlist_id, track_ids[i*100:100*(i+1)])
                
        

        
        return playlist_id, spotify_url