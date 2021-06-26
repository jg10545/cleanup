#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:35:11 2021

@author: joe
"""
import numpy as np
import sklearn.ensemble, sklearn.manifold
import logging


def get_distance_matrix(model, testdata):
    """
    Generate a matrix of "distances" for test dataset with respect to an
    ensemble model- where pairs of data points that were frequently assigned
    to the same leaf should have a lower distance.
    
    :model: a trained sklearn RandomForestRegressor model
    :testdata: an (N,d) numpy array of training data
    
    Returns an (N,N) array of pairwise distances.
    """
    # <--- snip
    N = testdata.shape[0]
    if N > 10000:
        logging.warn("you sure you want this much test data? this function may take a while to run")
    similarity_matrix = np.zeros((N,N))
    
    # for each tree
    for e in model.estimators_:
        # the tree.apply() function outputs the index of the leaf node
        leaf_ids = e.tree_.apply(testdata.astype(np.float32))
        # iterate through every pair of test points i and j
        for i in range(N):
            for j in range(i):
                # if i and j are in the same leaf node, increment the matrix
                if leaf_ids[i] == leaf_ids[j]:
                    similarity_matrix[i,j] += 1
                    similarity_matrix[j,i] += 1
    distance_matrix = np.log(similarity_matrix+1).max() - np.log(similarity_matrix+1)
    # <--- end snip
    return distance_matrix


def random_forest_embeddings(X_train, X_test, Y_train, Y_test, n_estimators=100):
    """
    Train a random forest regressor, find pairwise distances for a similarity
    plot and return T-SNE embeddings.
    
    :X_train: (N,d) numpy array of training covariates
    :X_test: (N_t, d) numpy array of test covariates
    :Y_train: (N,) numpy array of training labels
    :Y_test: (N_t,) numpy array of test labels
    :n_estimators: number of trees for the ensemble model
    
    Returns
    :embeddings: (N_t, 2) numpy array of T-SNE embeddings for each test point.
    :residuals: (N_t,) numpy array of model prediction residuals for each test point.
    """
    # <-- snip
    logging.info(f"training random forest regressor with {n_estimators} trees")    
    model = sklearn.ensemble.RandomForestRegressor(n_estimators=100)
    model = model.fit(X_train, Y_train)
    
    logging.info("computing residuals on test data")
    y_hat = model.predict(X_test)
    residuals = y_hat - Y_test
    
    logging.info("computing pairwise distance matrix")
    distance_matrix = get_distance_matrix(model, X_test)
    
    logging.info("computing embeddings")
    tsne = sklearn.manifold.TSNE(metric="precomputed")
    embeddings = tsne.fit_transform(distance_matrix)
    # <--- end snip
    return embeddings, residuals





