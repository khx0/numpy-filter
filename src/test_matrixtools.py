#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-04-12
# file: test_matrixtools.py
##########################################################################################

import os
import sys
import numpy as np
import unittest

from matrixtools import fillSymmetricMatrix
    
class MatrixtoolsTest(unittest.TestCase):
    
    """
    Test cases for the matrix-tools module
    gt = ground truth
    """
    
    def test_01(self):
    
        X = np.zeros((1, 1))
        res = fillSymmetricMatrix(X)    
        self.assertTrue(np.array_equal(res, X))
        
        X = np.zeros((1, 1))
        X[0, 0] = 1.0
        res = fillSymmetricMatrix(X)    
        self.assertTrue(np.array_equal(res, X))
        
        X = np.zeros((1, 1))
        X[0, 0] = -99.99
        res = fillSymmetricMatrix(X)    
        self.assertTrue(np.array_equal(res, X))
        
        X = np.zeros((2, 2))
        res = fillSymmetricMatrix(X)
        self.assertTrue(np.array_equal(res, X))
        
        X = np.eye(2)
        res = fillSymmetricMatrix(X)
        self.assertTrue(np.array_equal(res, X))
    
        X = np.zeros((2, 2))
        X[0, 0] = 1.0
        X[0, 1] = 2.0
        X[1, 1] = 4.0
        res = fillSymmetricMatrix(X)
        gt = np.zeros((2, 2))
        gt[0, 0] = 1.0
        gt[0, 1] = 2.0
        gt[1, 0] = 2.0
        gt[1, 1] = 4.0
        self.assertTrue(np.array_equal(res, gt))
        
        
        X = np.zeros((3, 3))
        X[0, 0] = 1.0
        X[0, 1] = 2.0
        X[0, 2] = 3.0
        X[1, 1] = 4.0
        X[1, 2] = 5.0
        X[2, 2] = 6.0
        
        res = fillSymmetricMatrix(X)
        gt = np.zeros((3, 3))
        gt[0, 0] = 1.0
        gt[0, 1] = 2.0
        gt[1, 0] = 2.0
        gt[0, 2] = 3.0
        gt[2, 0] = 3.0
        gt[1, 1] = 4.0
        gt[1, 2] = 5.0
        gt[2, 1] = 5.0
        gt[2, 2] = 6.0
        self.assertTrue(np.array_equal(res, gt))
  
        print(X)
        print(gt)
    
        return None

if __name__ == '__main__':

    unittest.main()
