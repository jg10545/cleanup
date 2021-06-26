#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:10:31 2021

@author: joe
"""
import pandas as pd
import sklearn.model_selection
import logging


def load_and_preprocess(filepath, target_col="price", split=0.1):
    """
    Load a CSV file containing our data, preprocess it, and split into train
    and test components.
    
    :filepath: string; path to CSV file
    :target_col: string; name of column containing our dependent variable
    :split: float; fraction of data to devote to testing
    
    Returns
    :X_train: 2D numpy array of training examples
    :X_test: 2D numpy array of test examples
    :Y_train: 1D numpy array of training labels
    :Y_test: 1D numpy array of test labels
    """
    # <--- snip
    df = pd.read_csv(filepath)
    for c in ["Latitude", "Longitude", "lat", "lon", "latitude", "longitude", "Lat", "Lon"]:
        if c in df.columns:
            logging.info(f"removing column {c}")
            df = df.drop(c, 1)
    
    if target_col not in df.columns:
        logging.error(f"target column {target_col} isn't even in this dataset. how are you so basic?")
    Y = df[target_col].values
    X = df[[c for c in df.columns if c != target_col]].values

    X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y,
                                                                        test_size=split)
    logging.debug("X_train:, %s"%str(X_train.shape))
    logging.debug("X_test:, %s"%str(X_test.shape))
    logging.debug("Y_train:, %s"%str(Y_train.shape))
    logging.debug("Y_test:, %s"%str(Y_test.shape))
    # <--- end snip
    return X_train, X_test, Y_train, Y_test

