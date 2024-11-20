'''Sub file'''

import decimal
from math import pi

def function_1():
    '''Will provide with output'''
    print('=' * 40)
    dec_1()
    dec_2()

def dec_1():
    '''Func 1'''
    x = 0.1
    summary = x + x + x
    print(f'Nomral sum of {x} + {x} + {x} is {summary}')
    x = decimal.Decimal(str(x))
    summary = x + x + x
    print(f'Sum with the use of Deciaml is {summary}')

def dec_2():
    '''Second function'''
    x = decimal.Decimal(str(pi))
    print(f'First 10 digits of pi are: {x.quantize(decimal.Decimal('1.000000000'))}')
