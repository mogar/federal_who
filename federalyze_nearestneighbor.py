#!/usr/bin/env python3

import re
from pathlib import Path
from collections import Counter
import numpy as np

authors = ['AlexanderHamilton', 'JamesMadison', 'JohnJay']

    
def hist_nearest_neighbor():
    '''Find nearest histogram neighbor for unknown papers'''
    # set up our tracking variables
    author_hists = {} #TODO: joy, madison, hamilton hists (maybe see numpy or something?)
    unknown_hists = {} # TODO: dict from paper num to histogram
    
    # iterate through all Federalist Papers files
    for author in authors:
        pathlist = Path('./papers/' + author).glob('*.txt')
        for path in pathlist:
            # because path is object not string
            fpath = str(path)
            
            f = open(fpath, "r")
            paper = f.read()
            f.close()

            # clean up the string
            paper = " ".join(paper.split("\n")[11:]) # first 11 lines are metadata
            paper = paper.lower()

            # add this to correct hist in author_hists
            if author in author_hists:
                author_hists[author].update(paper)
            else:
                author_hists[author] = Counter(paper)

        # now we normalize the collections
        total = sum(author_hists[author].values(), 0.0)
        for key in author_hists[author]:
                author_hists[author][key] /= total


    unknown_list = Path('./papers/unknown/').glob('*.txt')          
    for path in unknown_list:
        # because path is object not string
        fpath = str(path)
        print("file: " + fpath)
            
        f = open(fpath, "r")
        paper = f.read()
        f.close()

        # clean up the string
        paper = " ".join(paper.split("\n")[11:]) # first 11 lines are metadata
        paper = paper.lower()

        unknown_hists[fpath] = Counter(paper)
        # now we normalize the collection
        total = sum(unknown_hists[fpath].values(), 0.0)
        for key in unknown_hists[fpath]:
                unknown_hists[fpath][key] /= total

        # now we find nearest neighbor
        guess = ""
        min_val = 1
        for author in authors:
            words = set()
            words.update(author_hists[author].keys())
            words.update(unknown_hists[fpath].keys())

            distance = 0.0
            for word in words:
                distance += abs(unknown_hists[fpath][word] - author_hists[author][word])

            if distance < min_val:
                min_val = distance
                guess = author
            print("* Distance to " + author + ": " + str(distance))
        print("* Guess at Author: " + guess)


if __name__ == "__main__":
    print("# Histogram Nearest Neighbor")
    hist_nearest_neighbor()