#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:52:10 2021

@author: joe
"""
import numpy as np
import matplotlib
import os

from cleanup.plot import build_embedding_figure



def test_build_embedding_figure_returns_fig():
    N = 100
    embeddings = np.random.normal(0, 1, (N,2))
    residuals = np.random.normal(0, 2, (N,))
    
    fig = build_embedding_figure(embeddings, residuals)
    assert isinstance(fig, matplotlib.figure.Figure)
    
    
def test_build_embedding_figure_saves_fig(tmpdir):
    N = 100
    embeddings = np.random.normal(0, 1, (N,2))
    residuals = np.random.normal(0, 2, (N,))
    
    saveloc = os.path.join(tmpdir, "fig.jpg")
    
    output = build_embedding_figure(embeddings, residuals, save=saveloc)
    assert output is None