#!/usr/bin/python
# -*- coding: utf-8 -*-
###############################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-01-23
# file: filter_sequential_duplicates.py
###############################################################################

import numpy as np

def get_multiplicity(X):
    '''
    multiplicity is a list of tuples.
    Each tuple has the format (index, multiplicity),
    where only multiple records, i.e. multiplicity >= 2 are recorded
    Non-multiple entries do not create a record in the multiplicity list.
    '''

    # initialization
    multiplicity = []
    reading = False
    start = None
    mult = None
    cc = 1 # start with second array element

    if len(X) <= 1: # corner case
        return []

    while cc < len(X):
        if (X[cc] == X[cc - 1]) and (reading == False):
            reading = True
            start = cc - 1  # set start index
            mult = 2        # minimal multiplicity is 2
        elif (X[cc] == X[cc - 1]) and (reading == True):
            mult += 1       # continue current token reading
        elif (X[cc] != X[cc - 1]) and (reading == True):
            reading = False # stop current token reading
            record = (start, mult)
            mult = None
            multiplicity.append(record)
        cc += 1

    # cover end corner cases
    if mult:
        record = (start, mult)
        multiplicity.append(record)

    return multiplicity

if __name__ == '__main__':

    pass

    # X = np.array([1, 1, 2, 3, 4, 5])
    # returns [(0, 2)]

    # X = np.array([1, 2, 2, 3, 4, 5])
    # returns [(1, 2)]

    # X = np.array([1, 2, 3, 4, 5, 5])
    # returns [(4, 2)]

    # X = np.array([1, 1, 2, 2, 3, 4, 5])
    # returns [(0, 2), (2, 2)]

    # X = np.array([])
    # returns []

    # X = np.array([3])
    # returns []

    # X = np.array([1, 1, 1, 2, 2, 2, 3, 1, 4, 5, 5, 1, 2, 2, 2])
    # returns [(0, 3), (3, 3), (9, 2), (12, 3)]

    # X = np.array([2, 2, 4, 4, 4, 4, 4])
    # returns [(0, 2), (2, 5)]

    # X = np.array([90, 100, 4, 4, 4, 1])
    # returns [(2, 3)]

    # multiplicity = get_multiplicity(X)
    # print(multiplicity)
