'''An ordinary SubFile'''

import math

def do_math():
    '''Will do math output here'''
    print('=' * 40)
    math_1()
    math_2()
    math_3()

def math_1():
    '''Func 1'''
    x = 120
    print(f'Cos({x}) = {math.cos(x)}')
    print(f'Accos(0.23457325) = {math.acos(0.23457325)}')

def math_2():
    '''Func 2'''
    x = 3.5
    print(f'Getting the smallest int out of {x} is {math.floor(x)}')
    print(f'The biggest possible int out of {x} is {math.ceil(x)} ')

def math_3():
    '''Will do smthing strange'''
    x = 26
    print(f'Cubic root of {x} is {math.cbrt(x)}')
    print(f'Converts {x} from radians to degrees {math.degrees(x)}')
