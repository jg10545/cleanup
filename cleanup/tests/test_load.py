#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:57:12 2021

@author: joe
"""
import numpy as np
import pytest
from cleanup.load import load_and_preprocess


def test_load_and_preprocess(test_csv):
    X_train, X_test, Y_train, Y_test = load_and_preprocess(test_csv)
    assert isinstance(X_train, np.ndarray)
    assert isinstance(X_test, np.ndarray)
    assert isinstance(Y_train, np.ndarray)
    assert isinstance(Y_test, np.ndarray)
    
    assert len(X_train.shape) == 2
    assert len(X_test.shape) == 2
    
    assert X_train.shape[1] == 2
    assert X_test.shape[1] == 2
    
    assert X_train.shape[0] == len(Y_train)
    assert X_test.shape[0] == len(Y_test)
    
    
    
"""
If there are really problematic mistakes that a user could make, your code should
be written to throw an error instead of just returning an incorrect result.

Obviously it's impossible to foresee all possible screw-ups- but if there are
big ones you know about, you can add a unit test to make sure your code
fails the right way:
"""
    
def test_load_and_preprocess_with_bad_column_name(test_csv):
    with pytest.raises(Exception):
        results = load_and_preprocess(test_csv, target_col="not_a_real_column")