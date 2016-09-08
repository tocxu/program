#!/usr/bin/python
from sys import argv

script = argv
count =argv
def fib(x):
    a=1
    b=1
    while b<x:
        print b,
        b,a=a,b+a
c=int(count)
fib(c)
