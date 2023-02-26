import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import time
import os

def save_mel_spectogram(file_path: str):
    """
    Function to convert mp3 file to mel spectrogram and save as image
    
    Args:
        file_path (str): path to mp3 file
    """
    print(file_path)
    # get the genre from the file path
    genre = re.search(r'samples\\(.*)\\mp3', file_path).group(1)
    # get the track name from the file path
    track = re.search(r'samples\\{}\\mp3\\(.*).mp3'.format(genre), file_path).group(1)

    # load the mp3 file
    y, sr = librosa.load(file_path)
    # convert to mel spectrogram
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
    # convert to log scale
    log_S = librosa.power_to_db(S, ref=np.max)
    # save the spectrogram as an image
    librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
    plt.axis('off')
    if not os.path.exists('samples/{}/img'.format(genre)):
        os.makedirs('samples/{}/img'.format(genre))
    plt.savefig('samples/{}/img/{}.png'.format(genre, track), bbox_inches='tight', pad_inches=0)

def file_complete(file_path: str)->bool:
    """
    Function to check if the file is complete

    Args:
        file_path (str): path to the file

    Returns:
        bool: True if the file is complete, False otherwise

    """
    size = os.path.getsize(file_path)
    while size != os.path.getsize(file_path):
        size = os.path.getsize(file_path)
        time
    return True


class MyHandler(FileSystemEventHandler):
    """
    Class to handle file system events
    """
    def on_created(self, event):
        """
        Function to handle file creation events and convert the mp3 file to a mel spectrogram
        """
        if event.src_path.endswith('.mp3'):
            time.sleep(2)

            save_mel_spectogram(event.src_path)

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(MyHandler(), path='samples\\', recursive=True)
    observer.start()
    print("Observer started")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()