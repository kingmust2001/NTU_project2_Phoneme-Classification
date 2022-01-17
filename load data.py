# -*- coding: utf-8 -*-
"""project 2 - Phoneme Classification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-aWHOMa0DClaMfdNVOce4ILDNkFHEtsh

## Download Data
Download data from google drive, then unzip it.

You should have `timit_11/train_11.npy`, `timit_11/train_label_11.npy`, and `timit_11/test_11.npy` after running this block.<br><br>
`timit_11/`
- `train_11.npy`: training data<br>
- `train_label_11.npy`: training label<br>
- `test_11.npy`:  testing data<br><br>
"""

!gdown --id '1HPkcmQmFGu-3OknddKIa5dNDsR05lIQR' --output data.zip
!unzip data.zip
!ls

#import os
#os.getcwd()

"""## import package

"""

import torch
import torch.nn as nn
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
#from sklearn.model_selection import train_test_split

"""## Preparing Data
Load the training and testing data from the `.npy` file (NumPy array).
"""

import numpy as np
print("Loading data...")

data_root = "./timit_11/"
train = np.load(data_root + "train_11.npy")
train_label = np.load(data_root + "train_label_11.npy")
test = np.load(data_root + "test_11.npy")

print(" size of training dataset:", train.shape, "\n", "size of testing dataset:", test.shape)

#train[:10,::]

"""## create Dataset

"""

class TIMITDataset(Dataset):
    def __init__(self, X, y=None):
        self.data = torch.from_numpy(X).float()
        if y is not None:
            y = y.astype(np.int)
            self.label = torch.LongTensor(y)
        else:
            self.label = None

    def __getitem__(self, idx):
        if self.label is not None:
            return self.data[idx], self.label[idx]
        else:
            return self.data[idx]

    def __len__(self):
        return len(self.data)

"""## split data"""

"""VAL_RATIO = 0.2
train_x, val_x, train_y, val_y = train_test_split(train, train_label, test_size = VAL_RATIO, random_state=42)
print('Size of training set: {}'.format(train_x.shape))
print('Size of validation set: {}'.format(val_x.shape))"""

VAL_RATIO = 0.2

percent = int(train.shape[0] * (1 - VAL_RATIO))
train_x, train_y, val_x, val_y = train[:percent], train_label[:percent], train[percent:], train_label[percent:]
print('Size of training set: {}'.format(train_x.shape))
print('Size of validation set: {}'.format(val_x.shape))

"""## create Dataloader"""

BATCH_SIZE = 64

train_set = TIMITDataset(train_x, train_y)
val_set = TIMITDataset(val_x, val_y)
train_loader = DataLoader(train_set, batch_size = BATCH_SIZE, shuffle = True) # only shuffle training set
val_loader = DataLoader(val_set, batch_size = BATCH_SIZE, shuffle=False)

"""## clean memory

Cleanup the unneeded variables to save memory.

notes: if you need to use these variables later, then you may remove this block or clean up unneeded variables later
the data size is quite huge, so be aware of memory usage in colab
"""

import gc

del train, train_label, train_x, train_y, val_x, val_y
gc.collect()
