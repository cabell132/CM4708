import torch
from data_loader import data_loader
from torch.autograd import Variable
from torch.utils.tensorboard import SummaryWriter as writer
import os
from tqdm import tqdm
from sklearn import metrics
import numpy as np
from model import ShortChunkCNN

dev=torch.device("cuda")
torch.set_default_tensor_type(torch.FloatTensor)

class Trainer(object):

    def __init__(self):
                
        self.train_loader, self.validation_loader, self.test_loader, self.n_classes = data_loader("samples", 224, batch_size=32)
        self.model = ShortChunkCNN(128, self.n_classes)

    
    def to_var(self, x):
        """Convert tensor to variable."""
        if torch.cuda.is_available():
            x = x.cuda()
        return Variable(x)
    
    def validation(self, best_metric, epoch):
        roc_auc, pr_auc, loss = self.get_validation_score(epoch)
        score = 1 - loss
        if score > best_metric:
            print('best model!')
            best_metric = score
            torch.save(self.model.state_dict(),
                       os.path.join(self.model_save_path, 'best_model.pth'))
        return best_metric
    
    def get_auc(self, est_array, gt_array):
        roc_aucs  = metrics.roc_auc_score(gt_array, est_array, average='macro')
        pr_aucs = metrics.average_precision_score(gt_array, est_array, average='macro')
        print('roc_auc: %.4f' % roc_aucs)
        print('pr_auc: %.4f' % pr_aucs)
        return roc_aucs, pr_aucs

    def get_validation_score(self, epoch):
        self.model = self.model.eval()
        est_array = []
        gt_array = []
        losses = []
        reconst_loss = torch.nn.BCELoss()
        index = 0
        data, labels = list(self.validation_loader)[0]
        for x, y in tqdm(zip(data, labels)):
            
            # forward
            #x = self.to_var(x)
            #ground_truth = self.y[int(ix)]
            #y = torch.tensor([ground_truth.astype('float32') for i in range(self.batch_size)]).cuda()
            out = self.model(x)
            loss = reconst_loss(out.float(), y.float())
            losses.append(float(loss.data))
            out = out.detach().cpu()
  
            # estimate
            estimated = np.array(out).mean(axis=0)
            est_array.append(estimated)
            gt_array.append(y.cpu())
            index += 1
        print("est_array: ", (est_array))
        print("gt_array: ", (gt_array))
        est_array, gt_array = np.array(est_array), np.array(gt_array)
        loss = np.mean(losses)
        print('loss: %.4f' % loss)

        roc_auc, pr_auc = self.get_auc(est_array, gt_array)
        writer.add_scalar('Loss/valid', loss, epoch)
        writer.add_scalar('AUC/ROC', roc_auc, epoch)
        writer.add_scalar('AUC/PR', pr_auc, epoch)
        return roc_auc, pr_auc, loss

    def train(self):

         

        # Define the loss function and optimizer
        loss_func = torch.nn.BCELoss()
        current_optimiser = "adam"
        optimiser = torch.optim.Adam(self.model.parameters(), lr=0.001, weight_decay=0.0001)
        best_metric = 0
        self.epochs = 10

        # start training
        for epoch in range(1, self.epochs + 1):
            self.model = self.model.train()
            for x, y in self.train_loader:
                # Convert torch tensor to Variable
                x = self.to_var(x)
                y = self.to_var(y)

                # Forward pass: Compute predicted y by passing x to the model
                y_pred = self.model.forward(x)

                # Compute and print loss
                #print('y_pred: ', y_pred.dtype)
                #print('y: ', y.dtype)
                loss = loss_func(y_pred.float(), y.float())
                print('epoch: ', epoch,' loss: ', loss.item())

                # Zero gradients, perform a backward pass, and update the weights.
                optimiser.zero_grad()
                loss.backward()
                optimiser.step()
                
            #writer.add_scalar('Loss/train', loss.item(), epoch)

            # validation
            best_metric = self.validation(best_metric, epoch)

            