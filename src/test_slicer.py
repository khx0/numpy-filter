#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-02-09
# file: test_slicer.py
##########################################################################################

import os
import sys
import numpy as np
import unittest

from slicer import getMonotonicSubIntervals

class SlicerTest(unittest.TestCase):
    
    """
    Test cases for the getMonotonicSubIntervals function.
    GT = ground truth
    """
    
    def test_01(self):
    
        X = [1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0]
        intervalsGT = [[1.0, 2.0, 3.0, 4.0], [4.0, 3.0, 2.0, 1.0]]
        indexListGT = [(0, 3), (3, 6)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))
        
    def test_02(self):
    
        X = [1.1, 1.1]
        intervalsGT = [[1.1, 1.1]]
        indexListGT = [(0, 1)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))
        
    def test_03(self):
    
        X = [1.1, 1.0]
        intervalsGT = [[1.1, 1.0]]
        indexListGT = [(0, 1)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_04(self):
    
        X = [1.0, 1.1]
        intervalsGT = [[1.0, 1.1]]
        indexListGT = [(0, 1)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_05(self):
    
        X = [1.0, 2.0, 3.0, 4.0, 5.0]
        intervalsGT = [[1.0, 2.0, 3.0, 4.0, 5.0]]
        indexListGT = [(0, 4)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))
        
    def test_06(self):
    
        X = [5.0, 4.0, 3.0, 2.0, 1.0]
        intervalsGT = [[5.0, 4.0, 3.0, 2.0, 1.0]]
        indexListGT = [(0, 4)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_07(self):
    
        X = [5.0, 4.0, 3.0, 3.0, 1.0]
        intervalsGT = [[5.0, 4.0, 3.0, 3.0, 1.0]]
        indexListGT = [(0, 4)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))
        
    def test_08(self):
    
        X = [1.0, 2.0, 2.0, 3.0, 4.0]
        intervalsGT = [[1.0, 2.0, 2.0, 3.0, 4.0]]
        indexListGT = [(0, 4)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))
        
    def test_09(self):
    
        X = [1.0, 1.0, 1.0, 1.0, 1.0]
        intervalsGT = [[1.0, 1.0, 1.0, 1.0, 1.0]]
        indexListGT = [(0, 4)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_10(self):
    
        X = [1.0, 1.0, 1.0, 1.0, 5.0]
        intervalsGT = [[1.0, 1.0, 1.0, 1.0, 5.0]]
        indexListGT = [(0, 4)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_11(self):
    
        X = [1.0, 1.0, 1.0, 1.0, 0.0]
        intervalsGT = [[1.0, 1.0, 1.0, 1.0, 0.0]]
        indexListGT = [(0, 4)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))
        
    def test_12(self):
    
        X = [1.0, 1.0, 0.0, 1.0]
        intervalsGT = [[1.0, 1.0,  0.0], [0.0, 1.0]]
        indexListGT = [(0, 2), (2, 3)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))
        
    def test_13(self):
    
        X = [1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 0.0]
        intervalsGT = [[1.0, 1.0, 1.0, 1.0, 2.0, 2.0,], [2.0, 0.0]]
        indexListGT = [(0, 5), (5, 6)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_14(self):
    
        X = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        intervalsGT = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        indexListGT = [(0, 6)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_15(self):
    
        X = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        intervalsGT = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        indexListGT = [(0, 6)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_16(self):
    
        X = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        intervalsGT = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0]]
        indexListGT = [(0, 5), (5, 6)]
        
        intervals, indexList = getMonotonicSubIntervals(X)
    
        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

if __name__ == '__main__':

    unittest.main()




    
    
    
    
    
    
    
    
    
    
    
    