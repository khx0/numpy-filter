#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-01-08
# file: test_filter.py
##########################################################################################

import os
import sys
import numpy as np
import unittest

from filter import getNeighborAverage
from filter import filter_B_from_A_rowwise

class FilterTest(unittest.TestCase):
    
    """
    Test cases for the getNeighborAverage function.
    """
    
    def test_01(self):
    
        X = np.array([np.nan, 2.0])
    
        self.assertEqual(getNeighborAverage(X, 0), 2.0)
    
    def test_02(self):
    
        X = np.array([1.0, np.nan])

        self.assertEqual(getNeighborAverage(X, 1), 1.0)
        
    def test_03(self):
    
        X = np.array([1.0, np.nan, 3.0])

        self.assertEqual(getNeighborAverage(X, 1), 2.0)

    def test_04(self):
    
        X = np.array([1.0, np.nan, np.nan])

        self.assertEqual(getNeighborAverage(X, 1), 1.0)
        self.assertEqual(getNeighborAverage(X, 2), 1.0)

    def test_05(self):
    
        X = np.array([np.nan, np.nan, 3.0])

        self.assertEqual(getNeighborAverage(X, 0), 3.0)
        self.assertEqual(getNeighborAverage(X, 1), 3.0)
        
    def test_06(self):
    
        X = np.array([1.0, np.nan, np.nan, np.nan])

        self.assertEqual(getNeighborAverage(X, 1), 1.0)
        self.assertEqual(getNeighborAverage(X, 2), 1.0)
        self.assertEqual(getNeighborAverage(X, 3), 1.0)
        
    def test_07(self):
    
        X = np.array([np.nan, np.nan, np.nan, 4.0])

        self.assertEqual(getNeighborAverage(X, 0), 4.0)
        self.assertEqual(getNeighborAverage(X, 1), 4.0)
        self.assertEqual(getNeighborAverage(X, 2), 4.0)

    def test_08(self):
    
        X = np.array([np.nan, 2.0, 3.0, 4.0, 5.0])

        self.assertEqual(getNeighborAverage(X, 0), 2.0)

    def test_09(self):
    
        X = np.array([np.nan, 2.0, 3.0, 4.0, np.nan])

        self.assertEqual(getNeighborAverage(X, 0), 2.0)
        self.assertEqual(getNeighborAverage(X, 4), 4.0)
    
    def test_10(self):
    
        X = np.array([1.0, 2.0, np.nan, 4.0, np.nan])

        self.assertEqual(getNeighborAverage(X, 2), 3.0)
        self.assertEqual(getNeighborAverage(X, 4), 4.0)
        
    def test_11(self):
    
        X = np.array([1.0, np.nan, np.nan, 4.0, 5.0])

        self.assertEqual(getNeighborAverage(X, 1), 1.0)
        self.assertEqual(getNeighborAverage(X, 2), 4.0)
        
    def test_12(self):
    
        X = np.array([1.0, np.nan, 3.0, np.nan, 5.0])

        self.assertEqual(getNeighborAverage(X, 1), 2.0)
        self.assertEqual(getNeighborAverage(X, 3), 4.0)

    def test_13(self):
    
        X = np.array([np.nan, np.nan, np.nan, 4.0, 5.0, np.nan, np.nan, np.nan, np.nan, 10.0])

        self.assertEqual(getNeighborAverage(X, 0), 4.0)
        self.assertEqual(getNeighborAverage(X, 1), 4.0)
        self.assertEqual(getNeighborAverage(X, 2), 4.0)
        self.assertEqual(getNeighborAverage(X, 5), 5.0)
        self.assertEqual(getNeighborAverage(X, 6), 5.0)
        self.assertEqual(getNeighborAverage(X, 7), 10.0)
        self.assertEqual(getNeighborAverage(X, 8), 10.0)
        
    def test_14(self):
    
        X = np.array([np.nan, 2.0, 3.0, np.nan, 4.0, np.nan])

        self.assertEqual(getNeighborAverage(X, 0), 2.0)
        self.assertEqual(getNeighborAverage(X, 3), 3.5)
        self.assertEqual(getNeighborAverage(X, 5), 4.0)    
    
    def test_15(self):
        
        X = np.array([np.nan, np.nan])
        self.assertEqual(getNeighborAverage(X, 0), None)
        self.assertEqual(getNeighborAverage(X, 1), None)
        
        X = np.array([np.nan, np.nan, np.nan])
        self.assertEqual(getNeighborAverage(X, 0), None)
        self.assertEqual(getNeighborAverage(X, 1), None)
        self.assertEqual(getNeighborAverage(X, 2), None)
        
        X = np.array([np.nan, np.nan, np.nan, np.nan])
        self.assertEqual(getNeighborAverage(X, 0), None)
        self.assertEqual(getNeighborAverage(X, 1), None)
        self.assertEqual(getNeighborAverage(X, 2), None)
        self.assertEqual(getNeighborAverage(X, 3), None)
    
    def test_rowwise_filter_01(self):
        
        A = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

        B = np.array([[0, 0, 3],
                      [4, 5, 6],
                      [7, 0, 0]])
                  
        X = filter_B_from_A_rowwise(A, B)
    
        res = np.array([[1, 2, 3],
                        [7, 8, 9]])
        
        f1 = np.array_equal(X, res)
        f2 = (X.shape == res.shape) 
        
        self.assertEqual(f1, True)
        self.assertEqual(f2, True)

    def test_rowwise_filter_02(self):
        
        A = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

        B = np.array([[4, 5, 6],
                      [4, 5, 6],
                      [4, 5, 6]])
                  
        X = filter_B_from_A_rowwise(A, B)
    
        res = np.array([[1, 2, 3],
                        [7, 8, 9]])
        
        f1 = np.array_equal(X, res)
        f2 = (X.shape == res.shape) 
        
        self.assertEqual(f1, True)
        self.assertEqual(f2, True)
        
    def test_rowwise_filter_03(self):
        
        A = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

        B = np.array([[4, 5, 6],
                      [4, 5, 6],
                      [4, 5, 6],
                      [4, 5, 6],
                      [4, 5, 6]])
                  
        X = filter_B_from_A_rowwise(A, B)
    
        res = np.array([[1, 2, 3],
                        [7, 8, 9]])
        
        f1 = np.array_equal(X, res)
        f2 = (X.shape == res.shape) 
        
        self.assertEqual(f1, True)
        self.assertEqual(f2, True)
        
    def test_rowwise_filter_04(self):
        
        A = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
        
        B = np.array([[1, 5, 6],
                      [2, 5, 6],
                      [3, 5, 6],
                      [0, 5, 6],
                      [5, 5, 6]])
                  
        X = filter_B_from_A_rowwise(A, B)
    
        res = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
        
        f1 = np.array_equal(X, res)
        f2 = (X.shape == res.shape) 
        
        self.assertEqual(f1, True)
        self.assertEqual(f2, True)
        
    def test_rowwise_filter_05(self):
        
        A = np.array([[1, 2, 3],
                      [4, 5, 6]])
        
        B = np.array([[1, 2, 3],
                      [4, 5, 6]])
                
        X = filter_B_from_A_rowwise(A, B)
        
        res = np.empty((0, 3))
        
        f1 = np.array_equal(X, res)
        f2 = (X.shape == res.shape) 
        
        self.assertEqual(f1, True)
        self.assertEqual(f2, True)
        
    def test_rowwise_filter_06(self):
        
        A = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
    
        B = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [1, 2, 3]])
                  
        X = filter_B_from_A_rowwise(A, B)
        
        res = np.array([[7, 8, 9]])
        
        f1 = np.array_equal(X, res)
        f2 = (X.shape == res.shape) 
        
        self.assertEqual(f1, True)
        self.assertEqual(f2, True)
        
    def test_rowwise_filter_07(self):
        
        A = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
        
        B = np.array([[1, 2],
                      [3, 4],
                      [5, 6]])
                  
        X = filter_B_from_A_rowwise(A, B)
        
        res = A
        
        f1 = np.array_equal(X, res)
        f2 = (X.shape == res.shape) 
        
        self.assertEqual(f1, True)
        self.assertEqual(f2, True)        

if __name__ == '__main__':

    unittest.main()




    
    
    
    
    
    
    
    
    
    
    
    
    
