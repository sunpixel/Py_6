'''Sub file'''

import locale as l

def localize():
    '''Function'''
    print('=' * 40)
    loc_1()
    loc_2()
    loc_3()


def loc_1():
    '''Localization of currency'''
    x = 1256.23
    l.setlocale(l.LC_MONETARY, 'de')
    formatted = l.currency(x)
    print(f'This is how {x} is written in the specified country: {formatted}')

def loc_2():
    '''Localiztion of string'''
    x = 123213124124210000000000
    l.setlocale(l.LC_NUMERIC, 'en-gb')
    fromatted = l.format_string('%e',x)
    print(fromatted)

def loc_3():
    '''Getting local'''
    x = 12.40376
    l.setlocale(l.LC_ALL, '')
    formatted = l.format_string('%d', x)
    print(formatted)
