#!/usr/bin/env python3
""" cdrand() changes to a random directory
If there is no argument, and there is at least one directory in the
current working directory, it changes to that.  If there is an argument,
it should be the string representation of a valid path to a directory
and the random change will be from the directories in the argument."""

import sys
sys.dont_write_bytecode = True

import logging as l
l.basicConfig(level = 'DEBUG')
l.debug("Logging cdrand() begun")


import os
import random  


def cdrand(*path):
    if path:
        os.chdir(path)
    # same code whether arg or not now.
    contents = os.listdir()
    dirlist = []
    for entry in contents:
        if os.path.isdir(entry):
            dirlist.append(entry)
    if len(dirlist) > 1:
        newdir = random.choice(dirlist)
        os.chdir(newdir) 
        return newdir
    elif len(dirlist) == 1:
        newdir = path 
        return newdir
    else:
        return None

def main():
    here = os.getcwd()
    print("Start: " + here)
    newdir = cdrand()
    print("new directory: " + newdir)
    finish = os.getcwd()
    print("Finish: " + finish)
    

if __name__ == "__main__": main()
