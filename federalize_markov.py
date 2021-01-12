#!/usr/bin/env python3

import re
from pathlib import Path
from collections import Counter
import numpy as np
   
authors = ['AlexanderHamilton', 'JamesMadison', 'JohnJay']

def get_author(paper_str):
    '''
    Get the author of the given Federalist Paper
    Assumed to be stored in the string with the format: <p>Author: <strong>author_name</strong></p>
    returns "?" if the author is unknown
    '''
    return ""
    
def markov_compare():
    '''Run Baye's rule word by work on a Markov Chain for each author'''
    # set up our tracking variables
    author_model = {} # joy, madison, hamilton Markov chains
    unknown_paper = [] # dict from paper num to Markov chain
    
    # iterate through all Federalist Papers files
    # file iteration copied from: https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
    pathlist = Path(directory_in_str).glob('./papers/*.html')
    for path in pathlist:
        # because path is object not string
        fpath = str(path)
         
        f = open(fpath, "r")
        paper = f.read()
        f.close()
         
        author = get_author(paper)
        
        if author == "?":
            # not sure who wrote it, so add it to our questionable list
            unknown_paper.add(path)
        else:
            # add this to correct author model 
            if author in author_hists:
               author_model[author].
            else:
                author_model[author] = 
                  
    # do bayesian updating w markov model
    for paper in unknown_paper:
        f = open(paper, "r")
        paper = f.read()
        f.close()
        
        # TODO: Bayes' rule on chain updates
        
        # TODO: print results
        
if __name__ == "__main__":
    print("# Markov inverse probability")
    markov_compare()