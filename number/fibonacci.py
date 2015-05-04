#!/usr/bin/env python

class Fib(object):
    def __init__(self, n):
        self.n = n
    def __call__(self):
        l = [0, 1]
        for x in range(self.n - 2):
            l.append(l[-2] + l[-1])
        yield l
        
        
        
