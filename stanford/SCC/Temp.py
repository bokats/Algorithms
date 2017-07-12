# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 13:16:36 2017

@author: Bozhidar
"""

class test(object):
    
    def __init__(self, t):
        self.t = t
        
    def get_t(self):
        return self.t

b = test("bo")
b.t = "siyana"

print(b.get_t())