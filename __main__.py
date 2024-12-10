#!/usr/bin/env python

import random


def receive():
    if (random.randint(0, 1)):
        return 'recache'
    else:
        return 'recall'


def recall(rc):
    return (rc == 'recall')


def proceed(mem, counter):
    print(f'Proceeding with {mem} mem after {counter} loops')


def main():
    mem = None
    counter = 0
    rc = receive()
    while not mem:
        rc = receive()
        mem = (rc != 'recall')
        counter += 1
    proceed(mem, counter)


if __name__ == '__main__':
    main()
