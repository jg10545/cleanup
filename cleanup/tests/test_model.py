#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:10:36 2021

@author: joe
"""
import numpy as np
import sklearn.ensemble

from cleanup.model import get_distance_matrix, random_forest_embeddings


def test_get_distance_matrix_correct_output_types_and_shapes():
    # Goal for this unit test: make sure get_distance_matrix() runs
    # and outputs results that at least look plausible (a nonnegative
    # NxN array)
    
    # first generate a small fake dataset. I personally like to use
    # prime numbers for any dimensions in my inputs because it makes
    # debugging easier.
    N = 7
    d = 3
    X = np.random.normal(0, 1, (N,d))
    Y = np.random.normal(0, 1, (N,))
    # we need a trained model for the function to use. we don't need it to
    # be a GOOD model for the unit test, so just use a few estimators.
    n_estimators=5
    model = sklearn.ensemble.RandomForestRegressor(n_estimators=n_estimators)
    model.fit(X,Y)
    # now run the function we're actually testing
    dist_mat = get_distance_matrix(model, X)
    
    # finally, use `assert` to check that the following statements 
    # return True:
    
    # dist_mat is a numpy array
    assert isinstance(dist_mat, np.ndarray)
    # the distances are nonnegative
    assert dist_mat.min() >= 0
    # the matrix of distances should be NxN
    assert dist_mat.shape == (N,N)
    
    
def test_random_forest_embeddings():
    # <---- snip
    N = 7
    d = 3
    n_estimators=5
    
    X_train = np.random.normal(0, 1, (N,d))
    Y_train = np.random.normal(0, 1, (N,))
    X_test = np.random.normal(0, 1, (N,d))
    Y_test = np.random.normal(0, 1, (N,))
    
    embeddings, residuals = random_forest_embeddings(X_train, X_test, Y_train, Y_test,
                                                     n_estimators=n_estimators)
    
    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape == (N,2)
    assert isinstance(residuals, np.ndarray)
    assert residuals.shape == (N,)
    # <--- end snip