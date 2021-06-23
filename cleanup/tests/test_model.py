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
    N = 7
    d = 3
    n_estimators=5
    
    X = np.random.normal(0, 1, (N,d))
    Y = np.random.normal(0, 1, (N,))
    
    model = sklearn.ensemble.RandomForestRegressor(n_estimators=n_estimators)
    model.fit(X,Y)
    
    dist_mat = get_distance_matrix(model, X)
    
    assert isinstance(dist_mat, np.ndarray)
    assert dist_mat.min() >= 0
    assert dist_mat.shape == (N,N)