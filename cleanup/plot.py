#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:56:59 2021

@author: joe
"""
import numpy as np
import matplotlib.pyplot as plt
import logging



def build_embedding_figure(embeddings, residuals, threshold=1, alpha=0.5, save=False):
    """
    Use matplotlib to visualize embeddings
    
    :embeddings: (N,2) numpy array of T-SNE (or other) embeddings
    :residuals: (N,) numpy array of model test residuals
    :threshold: float; examples with residuals whose magnitude is greater than
        this threshold are considered "large error"
    :alpha: transparency value for plotting
    :save: add a filepath here to save figure to file instead of returning
    
    Returns
    :fig: matplotlib Figure, unless save != False
    """
    # <--- snip
    high_error = np.abs(residuals) > 1
    if high_error.sum() < 0.1*embeddings.shape[0]:
        logging.warn("high-error cases are under 10 percent of total")
    elif high_error.sum() > 0.5*embeddings.shape[0]:
        logging.warn("high-error cases are more than half of total")
    
    fig, ax = plt.subplots()
    ax.scatter(embeddings[~high_error,0], embeddings[~high_error,1], 
               alpha=alpha, marker=".",
           label="small error")
    ax.scatter(embeddings[high_error,0], embeddings[high_error,1], alpha=alpha, 
               marker="s",
           label="large error")
    ax.legend(loc="upper right")
    ax.axis(False)
    # <--- end snip
    if save:
        fig.savefig(save)
    else:
        return fig