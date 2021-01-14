#!/usr/bin/env python3

import re
from pathlib import Path
from collections import Counter
import numpy as np

from scipy.sparse import dok_matrix

authors = ['AlexanderHamilton', 'JamesMadison', 'JohnJay']

def clean_text(paper):
    paper = paper.lower()
    paper = paper.replace('\n',' ')
    paper = paper.replace('\t',' ')
    paper = paper.replace('“', ' " ')
    paper = paper.replace('”', ' " ')
    for spaced in ['.','-',',','!','?','(','—',')']:
        paper = paper.replace(spaced, ' {0} '.format(spaced))
    return paper

k = 2 # markov history: next word is based on k prior words
    
def markov_compare():
    '''Create Markov chains for each author, then do word-wise Bayesian updating on the unkown texts'''
    # set up our tracking variables
    author_markovs = {}
    
    # iterate through all Federalist Papers files
    for author in authors:
        corpus = ""
        pathlist = Path('./papers/' + author).glob('*.txt')
        for path in pathlist:
            # because path is object not string
            fpath = str(path)
            
            f = open(fpath, "r")
            paper = f.read()
            f.close()

            # clean up the string
            paper = " ".join(paper.split("\n")[11:]) # first 11 lines are metadata
            paper = clean_text(paper)

            corpus += paper

        # we have all their text, now train the markov chain
        # using this link as guidance: https://www.kdnuggets.com/2019/11/markov-chains-train-text-generation.html
        corpus_words = corpus.split(' ')
        corpus_words= [word for word in corpus_words if word != '']
        sets_of_k_words = [ ' '.join(corpus_words[i:k]) for i, _ in enumerate(corpus_words[:-k])]

        sets_count = len(list(set(sets_of_k_words)))
        distinct_words = list(set(corpus_words))
        next_after_k_words_matrix = dok_matrix((sets_count, len(distinct_words)))
        distinct_sets_of_k_words = list(set(sets_of_k_words))
        k_words_idx_dict = {word: i for i, word in enumerate(distinct_sets_of_k_words)}
        word_idx_dict = {word: i for i, word in enumerate(distinct_words)}
        for i, word in enumerate(sets_of_k_words[:-k]):
            word_sequence_idx = k_words_idx_dict[word]
            next_word_idx = word_idx_dict[corpus_words[i+k]]
            next_after_k_words_matrix[word_sequence_idx, next_word_idx] +=1

        # we now have our matrix, but we need to normalize it
        for word_sequence in sets_of_k_words[:-k]:
            next_word_vector = next_after_k_words_matrix[k_words_idx_dict[word_sequence]]
            next_after_k_words_matrix[k_words_idx_dict[word_sequence]] = next_word_vector/next_word_vector.sum()
        epsilon = .001*next_after_k_words_matrix.min() # TODO: Fix this

        # TODO: what parts of this to keep for the author?
        # add this to correct hist in author_hists
        author_markovs[author] = (word_idx_dict, k_words_idx_dict, next_after_k_words_matrix, epsilon)



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
        paper = clean_text(paper)

        # get our prior        
        for author in authors:
            P[author] = 1.0/len(authors)

        # now we use Bayes rule to sequentially update our (uniform) prior on authors, word by word
        for i in range(len(paper) - k):
            word_sequence = paper[i:i+k-1]
            next_word = paper[i+k]

            Pb = 0
            for author in authors:
                Pba = 0
                word_idx_dict = author_markovs[author][0]
                if next_word in word_idx_dict:
                    k_words_idx_dict = author_markovs[author][1]
                    next_after_k_words_matrix = author_markovs[author][2]
                    next_word_vector = next_after_k_words_matrix[k_words_idx_dict[word_sequence]]
                    p_idx = word_idx_dict.index[next_word]
                    Pba = next_word_vector[p_idx]
                if Pba == 0:
                    Pba = author_markovs[author][3] # epsilon
                P[author] = Pba * P[author]
                # track normalization constant
                Pb += Pba

            # normalize
            for author in authors:
                P[author] /= Pb

        for author in authors:
            print("* " + author + ": " + P[author])

        
if __name__ == "__main__":
    print("# Markov inverse probability")
    markov_compare()