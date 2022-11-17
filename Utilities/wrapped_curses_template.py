#!/usr/bin/env python3 -B
"""
Use the wrapper for curses setup and teardown.  It will leave the terminal
sane if you get an exception.  (I hope...)"""

import curses
from curses import wrapper

def main(stdscr):
                    # Clear screen
    stdscr.clear()
            # Proceed with your program
    print("Replace with your program")

# wrapper is a function that does all of the setup and teardown, and makes sure
# your program cleans up properly if it errors!
wrapper(main)
