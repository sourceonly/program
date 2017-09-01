#!/bin/env python
def identy(string):
    print string;
    
def unity(string):
    return 1

def line_op(string,op=identy):
    return apply(op,(string,))

def file_op(filename,lineop):
    print filename;
    f=open(filename)
    res=None;
    try:
        res=map(lambda x:line_op(x,lineop),f)
    finally:
        f.close()
    return res


