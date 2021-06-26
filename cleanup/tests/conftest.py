#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:48:40 2021

@author: joe
"""
import os
import pytest


@pytest.fixture
def test_csv():
    rootdir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(rootdir, "fixtures", "fakedata.csv")
    