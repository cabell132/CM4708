import cv2
import numpy as np
import os
import re
from torch.utils import data

class AudioFolder(data.Dataset):
    """
    Class to load the data
    """
    def __init__(self, data_path: str, img_size: int):
        """
        Constructor for the AudioFolder class

        Args:
            data_path (str): path to the data
            img_size (int): size of the image
            channels (int): number of channels
            num_classes (int): number of classes
        """
        self.X, self.y = self.get_data(data_path, img_size)

    def __len__(self):
        """
        Function to get the length of the dataset

        Returns:
            int: length of the dataset
        """
        return len(self.X)

    def __getitem__(self, index: int)->tuple:
        """
        Function to get a sample from the dataset

        Args:
            index (int): index of the sample

        Returns:
            tuple: tuple containing:
                X (np.array): array containing the data
                y (np.array): array containing the label
        """
        return self.X[index], self.y[index]

    def get_data(self, data_path: str, img_size: int)->tuple:
        """
        Function to load the data and convert it to the correct format

        Args:
            data_path (str): path to the data
            img_size (int): size of the image


        Returns:
            tuple: tuple containing:
                X (np.array): array containing the data
                y (np.array): array containing the labels
        """
        X = []
        y = []
        for root, dirs, files in os.walk(data_path):
            if root.endswith("img"):
                # Get the genre from the file path
                genre = re.search(r'samples\\(.*)\\img', root).group(1)
                # Loop over the image files in the subfolder
                for img in files:
                    # load the image
                    img = cv2.imread(os.path.join(root, img))
                    # resize the image
                    img = cv2.resize(img, (img_size, img_size))
                    # convert to grayscale
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # add the image to the list
                    X.append(img)
                    # add the label to the list
                    y.append(genre)
        # convert the lists to numpy arrays
        X = np.array(X)
        y = np.array(y)
        # reshape the data
        X = X.reshape(X.shape[0], img_size, img_size)
        # convert the labels to one-hot encoding
        unique_labels, indices = np.unique(y, return_inverse=True)
        y = np.eye(len(unique_labels))[indices]
        
        # convert the data to float32
        X = X.astype(np.float32)
        return X, y

def data_loader(data_path: str, img_size: int, batch_size: int)->tuple:
    """
    Function to load the data

    Args:
        data_path (str): path to the data
        img_size (int): size of the image
        batch_size (int): batch size

    Returns:
        tuple: tuple containing:
            train_loader (DataLoader): train data loader
            test_loader (DataLoader): test data loader
            num_classes (int): number of classes
    """
    # create the dataset
    dataset = AudioFolder(data_path, img_size)
    # split the dataset into train and test, validation
    train_size = int(0.8 * len(dataset))
    validation_size = int(0.1 * len(dataset))
    test_size = len(dataset) - train_size - validation_size
    train_dataset, validation_dataset, test_dataset = data.random_split(dataset, [train_size, validation_size, test_size])
    # create the data loaders
    train_loader = data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    validation_loader = data.DataLoader(validation_dataset, batch_size=batch_size, shuffle=True)
    test_loader = data.DataLoader(test_dataset, batch_size=batch_size, shuffle=True)
    return train_loader, validation_loader, test_loader, len(dataset.y[0])