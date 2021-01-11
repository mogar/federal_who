#!/usr/bin/env python3

import re
from pathlib import Path
from collections import Counter
import numpy as np

def strip_html(html_str):
    '''Remove html tags from a string
    copied from: '''
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
    
# currently unused?
def hist_words(paper_str):
    '''Create a histogram of the words in the input string'''
    counts = Counter(paper_str)
    labels, values = zip(*counts.items())
    
    return (labels, values)
    
def get_author(paper_str):
    '''
    Get the author of the given Federalist Paper
    Assumed to be stored in the string with the format: <p>Author: <strong>author_name</strong></p>
    returns "?" if the author is unknown
    '''
    return ""
    
def hist_nearest_neighbor():
    '''Find nearest histogram neighbor for unknown papers'''
    # set up our tracking variables
    author_hists = {} #TODO: joy, madison, hamilton hists (maybe see numpy or something?)
    unknown_hists = {} # TODO: dict from paper num to histogram
    
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
            unknown_hists[path] = Counter(strip_html(paper))
        else:
            # add this to correct hist in author_hists
            if author in author_hists:
               author_hists[author].update(strip_html(paper))
            else:
                author_hists[author] = Counter(strip_html(paper))
                     
    for paper in unknown_hists:
        # TODO: get nearest neighbor 
        
        # TODO: print results
        
if __name__ == "__main__":
    print("# Histogram Nearest Neighbor")
    hist_nearest_neighbor()