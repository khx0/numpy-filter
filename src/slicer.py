#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-02-12
# file: slicer.py
##########################################################################################

import os
import sys
import numpy as np

def isMonotonicallyIncreasing(X):
    '''
    Takes a 1d numpy array X as input.
    Returns a boolean (True/False) depending on if X is in fact
    monotonically increasing or not.
    '''
    return np.all(X[1:] >= X[:-1])

def isStrictlyMonotonicallyIncreasing(X):
    '''
    Takes a 1d numpy array X as input.
    Returns a boolean (True/False) depending on if X is in fact 
    strictly monotonically increasing or not.
    '''
    return np.all(X[1:] > X[:-1]) 
    
def isMonotonicallyDecreasing(X):
    '''
    Takes a 1d numpy array X as input.
    Returns a boolean (True/False) depending on if X is in fact
    monotonically decreasing or not.
    '''
    return np.all(X[1:] <= X[:-1])

def isStrictlyMonotonicallyDecreasing(X):
    '''
    Takes a 1d numpy array X as input.
    Returns a boolean (True/False) depending on if X is in fact 
    strictly monotonically decreasing or not.
    '''
    return np.all(X[1:] < X[:-1]) 

def getMonotonicSubIntervals(X):
    '''
    Arguments:
        X: a 1D numpy array (with at least two entries)
    
    Returns:
        Intervals: A python list which contains non-strictly monotonic slices
                   of the original array X:
        indexList: A list of index pairs, which specify the indices of the slices
                   w.r.t to the original array X
    
    Splits the given input array X into (non-striclty) monotonic subintervals,
    while preserving the order of all elements of X.
    We assume X to contain only real valued entries.
    
    * If the input array is already non-decreasing or non-increasing (i.e. non-strictly
      monotonic) we return a list which contains the full input array X, i.e. the
      function will return [X].
    
    * If the input array has only two entries (len(X) == 2), then we equally return
      the full array X immediately (i.e. [X]), since two values are always non-strictly
      monotonous (they can only be equal, larger or smaller, but for two values there
      can be no change from increasing to decreasing or vice versa).
      
    * In all other cases the function returns a list which contains non-stricly monotonic
      slices of X, such that each slice in that list is non-stricly monotonic.
      
    * We emphasize that we use non-strict monotonicty, since we want to allow a series of
      values to be equal at some point.
      
    Example:

    Given the input array X as specified below:

    X = [1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0]
    
    the function will return
    
    intervals = [[1.0, 2.0, 3.0, 4.0],
                 [4.0, 3.0, 2.0, 1.0]]
                 
    indexList = [(0, 3), (3, 6)]

    '''
    
    # Subintervals make only sense for arrays which contain at least two entries.
    assert (len(X) >= 2), "Error: len(X) < 2."
    
    intervals = []
    indexList = []
    
    if (len(X) == 2):
        # Arrays of length 2 will always be non-stricly monotonic.
        intervals.append(X)
        indexList.append((0, (len(X) - 1)))
        return intervals, indexList
    elif (all(x >= y for x, y in zip(X, X[1:]))):
        # Directly return non-decreasing arrays.
        intervals.append(X)
        indexList.append((0, (len(X) - 1)))
        return intervals, indexList
    elif (all(x <= y for x, y in zip(X, X[1:]))):
        # Directly return non-increasing arrays.
        intervals.append(X)
        indexList.append((0, (len(X) - 1)))
        return intervals, indexList
    else:
        
        # In this else branch we deal with the case where there is actually some work
        # to do, i.e. we have at least one turning point.
    
        def Increasing(a, b):
            return (a >= b)
        def Decreasing(a, b):
            return (a <= b)
        
        ##################################################################################
        # Initialize the comparator function handle.
        # Notice the usage of the strict < or > signs here.
        # This is essential here to get the initial comparator right.
        # If we do not check this here we might default to a wrong comparator
        # if an input array starts with a bunch of equal entries.
        # Hence we need the strict < and > signs here although we do not 
        # require strict monotonicity in our final result.
        j = 0
        while (j < (len(X) - 1)):
            if (X[j + 1] > X[j]):
                comparator = Increasing
                break
            elif (X[j + 1] < X[j]):
                comparator = Decreasing
                break
            else:
                j += 1
        ##################################################################################
            
        leftIndex = 0
    
        # sweep the X array once to detect the turning points
        for i in np.arange(1, len(X) - 1, 1):
        
            if comparator(X[i + 1], X[i]):  
                continue
            else:
                indexList.append((leftIndex, i))
                intervals.append(X[leftIndex:(i + 1)])
                leftIndex = i
                if (X[i + 1] >= X[i]):
                    comparator = Increasing
                else:
                    comparator = Decreasing
    
        indexList.append((leftIndex, (len(X) - 1)))
        intervals.append(X[leftIndex:])
                
        return intervals, indexList 
    
if __name__ == '__main__':

    pass
