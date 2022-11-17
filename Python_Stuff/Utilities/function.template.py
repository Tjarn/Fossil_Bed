#!/usr/bin/env python3
""" docstring """

# keeps python3 from writing compliled code everywhere
import sys
sys.dont_write_bytecode = True
# end slapping down litter


def test(str):
    return str

def main():
    str = 'OK'
    assert test(str) == str

    print("If you get here, it passed")

if __name__ == "__main__": main()
