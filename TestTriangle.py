# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral')

    def testIsocelesTrianglesA(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classifyTriangle(3,4,3),'Isoceles')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene')

    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(10,15,12),'Scalene')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1,2,5),'NotATriangle')

    def testInvalidIputA(self):
        self.assertEqual(classifyTriangle(0,1,2),'InvalidInput')

    def testInvalidIputB(self):
        self.assertEqual(classifyTriangle(-1,2,3),'InvalidInput')

    def testValid200(self):
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(2.1,0.1,111),'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

