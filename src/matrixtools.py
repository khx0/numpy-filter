#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-04-13
# file: matrixtools.py
##########################################################################################

import numpy as np

def fillSymmetricMatrix(X):
    '''
    fillSymmetricMatrix routine
    This routine assumes that the input matrix/array is upper triangular
    with a filled diagonal like indicated below for a 5x5 example
    * * * * *           * * * * *
    - * * * *           * * * * *
    - - * * *   ===>    * * * * *
    - - - * *           * * * * *
    - - - - *           * * * * *
    where the "-" symbols indicate empty (non filled) values and the asteriskes "*" 
    symbols indicate filled values. Then the fillSymmetrixMatrix() function will return 
    the symmetic matrix where the diagonal is preserved and the lower triangular 
    is filled by their corresponding upper triangular values.
    '''
    assert X.shape[0] == X.shape[1], "Error: X is not quadratic."
    tmp = np.zeros_like(X)
    tmp[:] = np.transpose(X)
    np.fill_diagonal(tmp, 0.0) # assuming a square matrix!
    tmp = tmp + X              # adding the upper (with diagonal) to the lower triangular
    X = tmp
    return X
    
if __name__ == '__main__':

    pass

    
    
    
    
    
    
    
    
    
    
    
    
