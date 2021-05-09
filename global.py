#!/usr/bin/env python3
""" This script allows you to use and define
temporal global variables in yout terminal """

import pickle
from sys import argv
from os.path import exists


FILE = '/tmp/globals.tmp'


def read():
    """ Read all the variables stored """
    if not exists(FILE):
        return {}

    reader = open(FILE, 'rb')
    data = pickle.load(reader)
    reader.close()
    return data


def write(data):
    """ Save the variables """
    writer = open(FILE, 'wb')
    pickle.dump(data, writer)
    writer.close()


def main(args):
    """ Main function """
    if len(args) <= 1:
        return

    if len(args) == 3:
        if not args[2].strip():
            return

        data = read()
        data[args[1]] = args[2]
        write(data)
    else:
        print(dict.get(read(), args[1], ''), end='')


main(argv)
