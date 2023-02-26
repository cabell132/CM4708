import torch

# Define the CNN model
class ShortChunkCNN(torch.nn.Module):
    def __init__(self, n_channels, n_classes):
        super(ShortChunkCNN, self).__init__()

        
        # Define the first convolutional layer
        self.conv1 = torch.nn.Conv2d(1, n_channels, kernel_size=3, stride=1, padding=3//2).cuda()
        self.bn1 = torch.nn.BatchNorm2d(n_channels).cuda()
        self.relu1 = torch.nn.ReLU().cuda()
        self.pool1 = torch.nn.MaxPool2d(2).cuda()

        # Define the second convolutional layer
        self.conv2 = torch.nn.Conv2d(n_channels, n_channels, kernel_size=3, stride=1, padding=3//2).cuda()
        self.bn2 = torch.nn.BatchNorm2d(n_channels).cuda()
        self.relu2 = torch.nn.ReLU().cuda()
        self.pool2 = torch.nn.MaxPool2d(2).cuda()

        # Define the third convolutional layer
        self.conv3 = torch.nn.Conv2d(n_channels, n_channels*2, kernel_size=3, stride=1, padding=3//2).cuda()
        self.bn3 = torch.nn.BatchNorm2d(n_channels*2).cuda()
        self.relu3 = torch.nn.ReLU().cuda()
        self.pool3 = torch.nn.MaxPool2d(2).cuda()

        # Define the fourth convolutional layer
        self.conv4 = torch.nn.Conv2d(n_channels*2, n_channels*2, kernel_size=3, stride=1, padding=3//2).cuda()
        self.bn4 = torch.nn.BatchNorm2d(n_channels*2).cuda()
        self.relu4 = torch.nn.ReLU().cuda()
        self.pool4 = torch.nn.MaxPool2d(2).cuda()

        # Define the fifth convolutional layer
        self.conv5 = torch.nn.Conv2d(n_channels*2, n_channels*2, kernel_size=3, stride=1, padding=3//2).cuda()
        self.bn5 = torch.nn.BatchNorm2d(n_channels*2).cuda()
        self.relu5 = torch.nn.ReLU().cuda()
        self.pool5 = torch.nn.MaxPool2d(2).cuda()

        # Define the sixth convolutional layer
        self.conv6 = torch.nn.Conv2d(n_channels*2, n_channels*2, kernel_size=3, stride=1, padding=3//2).cuda()
        self.bn6 = torch.nn.BatchNorm2d(n_channels*2).cuda()
        self.relu6 = torch.nn.ReLU().cuda()
        self.pool6 = torch.nn.MaxPool2d(2).cuda()

        # Define the seventh convolutional layer
        self.conv7 = torch.nn.Conv2d(n_channels*2, n_channels*4, kernel_size=3, stride=1, padding=3//2).cuda()
        self.bn7 = torch.nn.BatchNorm2d(n_channels*4).cuda()
        self.relu7 = torch.nn.ReLU().cuda()
        self.pool7 = torch.nn.MaxPool2d(2).cuda()

        
        # Define the first dense layer
        self.dense1 = torch.nn.Linear(n_channels*4, n_channels*4).cuda()
        self.bn_dense = torch.nn.BatchNorm1d(n_channels*4).cuda()

        # Define the second dense layer
        self.dense2 = torch.nn.Linear(n_channels*4, n_classes).cuda()
        self.dropout = torch.nn.Dropout(0.5).cuda()
        self.relu_dense = torch.nn.ReLU().cuda()

    def forward(self, x):
        # Pass the input tensor through each of our operations

        #unsqueeze the input tensor
        x = x.unsqueeze(1)

        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu1(x)
        x = self.pool1(x)

        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu2(x)
        x = self.pool2(x)

        x = self.conv3(x)
        x = self.bn3(x)
        x = self.relu3(x)
        x = self.pool3(x)

        x = self.conv4(x)
        x = self.bn4(x)
        x = self.relu4(x)
        x = self.pool4(x)

        x = self.conv5(x)
        x = self.bn5(x)
        x = self.relu5(x)
        x = self.pool5(x)

        x = self.conv6(x)
        x = self.bn6(x)
        x = self.relu6(x)
        x = self.pool6(x)

        x = self.conv7(x)
        x = self.bn7(x)
        x = self.relu7(x)
        x = self.pool7(x)
        x = x.squeeze(2)

        # Global Max Pooling
        if x.size(-1) != 1:
            x = torch.nn.MaxPool1d(x.size(-1))(x)
        x = x.squeeze(2)

        x = self.dense1(x)
        x = self.bn_dense(x)
        x = self.relu_dense(x)
        x = self.dropout(x)
        x = self.dense2(x)
        x = torch.nn.Sigmoid()(x)

        return x