'''Sub file'''

from random import randint, random

def do_random():
    '''Main sub function of the file'''
    print('=' * 40)
    print(ran_1())
    print(ran_2())

def ran_1():
    '''Random float'''
    return random()

def ran_2():
    '''Random int in range'''
    return randint(-100, 100)
