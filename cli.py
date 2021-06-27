#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 23:05:23 2021

@author: joe
"""
import argparse
import logging
from cleanup.load import load_and_preprocess
from cleanup.model import random_forest_embeddings
from cleanup.plot import build_embedding_figure


def main():
    """
    Nothing fancy here. just runs the code we wrote and saves a figure to file.
    """
    # use argparse to gather inputs
    parser = argparse.ArgumentParser(description='Load data from a csv and save out a randomforestregressor similarity plot')
    parser.add_argument('inputfile', type=str, help='path to input CSV')
    parser.add_argument('--outputfile', type=str, help='location to save output to',
                        default='randomforest_similarity.jpg')
    parser.add_argument('--logging', type=str, help='logging threshold',
                        default='WARN')
    
    args = parser.parse_args()
    
    
    # set logging threshold
    logger = logging.getLogger()    
    logger.setLevel(args.logging)
    # load/preprocess data
    X_train, X_test, Y_train, Y_test = load_and_preprocess(args.inputfile,
                                                           target_col="price", 
                                                           split=0.1)
    # compute embeddings
    embeddings, residuals = random_forest_embeddings(X_train, X_test, Y_train, Y_test,
                                                     n_estimators=100)
    # visualize
    build_embedding_figure(embeddings, residuals, threshold=1., 
                           save=args.outputfile)
    
    
    
# this is what gets called if you run this python file from the command line
if __name__ == "__main__":
    main()
    
    