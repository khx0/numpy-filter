#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-01-23
# file: array_compression.py
# tested with python 3.7.6 and numpy 1.19.5
##########################################################################################

import numpy as np

def getDisjointIntervals(X: np.ndarray) -> list:
    """
    Takes a 1D list of integers X as input and returns a list of disjoint
    intervals, stating at which intervals X is non-zero.
    Performs a single pass over X.
    This is an example of a compressed representation of a (1d) integer array.
    """
    if len(X) == 0:
        return []
    else:
        cc = 0
        currentToken = -1
        intervals = []
        reading = False
        while cc < len(X):

            if (X[cc] > 0) and (not reading):
                idxLeft = cc
                currentToken = X[cc]
                reading = True

            elif (X[cc] != currentToken) and reading:
                idxRight = (cc - 1)
                record = (int(idxLeft), int(idxRight), int(currentToken))
                intervals.append(record)

                if X[cc] > 0:
                    idxLeft = cc
                    currentToken = X[cc]
                    reading = True
                else:
                    reading = False

            cc += 1

        # termination case
        if reading:
            assert cc == len(X)
            idxRight = cc - 1
            record = (int(idxLeft), int(idxRight), int(currentToken))
            intervals.append(record)

        return intervals

if __name__ == '__main__':

    pass
