#!/usr/bin/env python3
""" This script allows you to use and define
temporal global variables in yout terminal """

import pickle
from sys import argv
from os.path import exists
from os import environ as env


FILE = '/tmp/globals.tmp'
P_FILE = env.get('HOME') + '/.globals'


def read(path=FILE):
    """ Read all the variables stored """
    if not exists(path):
        return {}

    reader = open(path, 'rb')
    data = pickle.load(reader)
    reader.close()
    return data


def write(data, path=FILE):
    """ Save the variables """
    writer = open(path, 'wb')
    pickle.dump(data, writer)
    writer.close()


def main(args):
    """ Main function """
    if len(args) <= 1:
        return

    src = FILE
    if args[1] == '-p':
        args = [args[0]] + args[2:]
        src = P_FILE

    if len(args) == 3:
        if not args[2].strip():
            return

        data = read(src)
        data[args[1]] = args[2]
        write(data, src)
    else:
        print(dict.get(read(src), args[1], ''), end='')


main(argv)
