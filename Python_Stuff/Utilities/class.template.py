#!/usr/bin/env python3
''' docstring '''
# keeps python3 from writing compliled code everywhere
import sys
sys.dont_write_bytecode = True
# end slapping down litter

class Example:
    def __init__(self):
        self.name = 'example'
    def tell_name(self):
        return self.name

def main():
    foo = Example()
    print(foo.tell_name())
    assert foo.tell_name() == 'example'
    print('If you got here it passed')

if __name__ == "__main__": main()

