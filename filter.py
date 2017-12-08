#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2017-12-08
# file: filter.py
##########################################################################################

import os
import sys
import numpy as np

def getNeighborAverage(X, index):

    '''
    Arguments:
        X: a 1D numpy array
        index: index of an element of X, i.e. an integer value between 0 and len(X) - 1

    Returns the closest neighboring average value for the element at position index
    of a 1D array X, assuming that the element at position index is not a valid entry
    (e.g. here a np.nan value).

    Rationale:
    This function assumes, that some given data might be incomplete and this incomplete
    or missing elements have been assigned the np.nan value.
    To fill these voids, this function finds the closest neighbouring element and
    calculates the average of the left and right neighboring elements, if both are valid
    values. If only the left most or right most neighboring entry is valid, it takes
    only this value, respectively. If the closest neighboring pair is not valid (i.e. both
    are also np.nan values), it iterates outward to find the closes neighboring values.
    If this iteration fails to find any valid entry in the entire array X, the function
    will eventually terminate by returning None, after having passed through X once.

    At the moment this is only implemented for 1d numpy arrays X.

    Example:

    Given the input array X with six entries

    X = [np.nan, 2.0, 3.0, np.nan, 4.0, np.nan]

    This averaging method will return the following outputs.

        - getNeighborAverage(X = X, index = 0) = 2.0
        - getNeighborAverage(X = X, index = 3) = 3.5
        - getNeighborAverage(X = X, index = 5) = 4.0

    '''

    if (len(X) == 1):
        print "Error: Array of length 1 passed."
        sys.exit(1)

    if (index < 0 or index >= len(X)):
        print "Error: Index out of bounds."
        sys.exit(1)

    if (index == 0):
        # left border --> move to the right only
        cc = index + 1
        while (cc < len(X)):
            tmp = X[cc]
            if (not np.isnan(tmp)):
                return tmp
            else:
                cc += 1

    elif (index == (len(X) - 1)):
        # right border --> move to the left only
        cc = index - 1
        while (cc >= 0):
            tmp = X[cc]
            if (not np.isnan(tmp)):
                return tmp
            else:
                cc -= 1

    else:

        for cc in range(1, len(X)): # len(X) is here used as a safe upper bound

            if ((index - cc) >= 0) and ((index + cc) < len(X)):
                left, right = X[index - cc], X[index + cc]
                if ((not(np.isnan(left))) and (not(np.isnan(right)))):
                    return (left + right) / 2.0
                elif (not(np.isnan(left))):
                    return left
                elif (not(np.isnan(right))):
                    return right
                else:
                    continue
            elif (((index - cc) >= 0) and (index + cc) >= len(X)):
                left = X[index - cc]
                if (not np.isnan(left)):
                    return left
                else:
                    continue
            else:
                right = X[index + cc]
                if (not np.isnan(right)):
                    return right
                else:
                    continue

    return None
    
def filter_B_from_A_rowwise(A, B):

    '''
    Arguments:
        A and B are two numpy arrays of equal column numbers.

    Returns an array with equal column numbers where all rows in B, that also are
    contained in A are delted from A.

    Example:

    Given the input arrays A and B as
    
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    
    and
    
    B = [[0, 0, 3],
         [4, 5, 6],
         [7, 0, 0]]

    the function will return
    
    res = [[1, 2, 3],
           [7, 8, 9]]
           
    Comment:
    In the case of differing column numbers, this function should
    simply return the unaltered input array A, since the
    np.array_equal() funcion call never return True.
    '''

    nRowsA = A.shape[0]
    nRowsB = B.shape[0]
    
    row_indices = []

    for i in range(nRowsA):
        
        thisRow = A[i, :]
                
        for j in range(nRowsB):
        
            thatRow = B[j, :]
            
            if (np.array_equal(thisRow, thatRow)):
                row_indices.append(i)
            
    A = np.delete(A, row_indices, axis = 0)
    
    return A

if __name__ == '__main__':

    pass
