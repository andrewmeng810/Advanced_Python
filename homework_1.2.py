#!/usr/bin/env python3    # make sure this is the very first line, flush left!

"""
homework_1.2.py -- gererate a fibonacci series upto the user's number
Author: Qi Meng Qi.meng810@gmail.com
Last modified: 09.23.2017
"""

import sys

def take_input():
    """ take the input """
    try:
        argument = sys.argv[1]  # Take the argument from Command Line, and remove space
    except IndexError:
        exit('error: invalid input')
    return argument

def validate_input(argument):
    """ Validate input, exit if input not an integer """

    try:
        int_arg = int(argument)     # might raise a ValueError
    except ValueError:
        raise ValueError('please enter an integer')
    return int_arg

def fibonacci(int_arg):
    """ Create fibonacci series up to ini_arg """

    fir = 1
    sec = 1
    res = 2
    print(fir, end = ' ')
    print(sec, end = ' ')
    while res < int_arg:
        res = fir + sec
        print(sec,end = ' ')
        fir = sec
        sec = res


def main():
    argument = take_input()
    int_arg = validate_input(argument)
    fibonacci(int_arg)



if __name__ == '__main__':

    main()
    exit(0)   # exit, signaling no error
