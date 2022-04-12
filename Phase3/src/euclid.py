import pandas as pd
import numpy as np

def euclid(train_X, val_X):
    """
    :param train_X: one record from the training set
                    (type series or dataframe including target (survived))
    :param val_X: one record from the validation set
                    series or dataframe include target (survived)
    :return:
    """
    diff = train_X - val_X

    # Remove survived column
    diff = diff.iloc[:, :-1]

    dist = np.sqrt((diff ** 2).sum(axis=1))

    return dist
def manhattan(train_X, val_X):
    """
    :param train_X: one record from the training set
                    (type series or dataframe including target (survived))
    :param val_X: one record from the validation set
                    series or dataframe include target (survived)
    :return: the Manhattan distance between train_X and val_X
    """
    diff = train_X - val_X

    # Remove survived column
    diff = diff.iloc[:, :-1]

    dist = np.sqrt((np.abs(diff)).sum(axis=1))

    return dist

