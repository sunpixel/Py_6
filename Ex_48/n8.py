# pylint:disable = C2801
'''The Data Class module'''

from random import randint
from dataclasses import dataclass

@dataclass
class User:
    '''User class'''
    id: int
    login: str
    password: str

@dataclass(unsafe_hash=True)
class Dog:
    '''Class representing a dog'''
    breed: str
    age: int
    sex: str
    vaccinated: bool = False

@dataclass(order=True)
class Plane:
    '''Reperesent an aircraft'''
    type: str
    age: int
    model: float
    capacity: int
    top_speed: int = 990

user1 = User(123, 'Loser123', '321')
dog1 = Dog('German Shepard', 4, 'Male')
aircraft1 = Plane('AirBus', 12, 'A380A', 560)

def function_1():
    '''Will do things'''
    print('=' * 40)
    print(user1)
    print(f'Hashed class object of god is {dog1.__hash__()}')
    print(f'No hash {dog1}')
    print(aircraft1)
    print('=' * 40)
    fun_1([user1, dog1, aircraft1])
    fun_2([user1, dog1, aircraft1])
    fun_3(user1)
    fun_4('Boeing', 5, '747', 500, 900)

def fun_1(craft):   # Is num 1 and 2
    '''Processes a list of dataclass objects and prints their attributes'''
    print('=' * 40)
    def sub(obj):
        '''Extracts key-value pairs from an object's dict and returns them as a list of strings'''
        x = list()
        for key, val in vars(obj).items():
            x.append(f'{key} : {val}')
        return x

    x = craft
    if isinstance(x, list):
        for i in x:
            print(sub(i))
    else:
        print(sub(x))

def fun_2(obj):
    '''Makes a dictionary with key-value pairs using dataclass object as value'''
    print('=' * 40)
    x = dict()
    i = 0
    if isinstance(obj, list):
        for k in obj:
            x[i] = k
            i += 1
        print(x)

def fun_3(obj):
    '''Perfroms data class modifications'''
    x = []
    for key, val in vars(obj).items():
        x.append(key)
    i = randint(0, len(x) - 1)
    if hasattr(obj, x[i]):
        print(f'Random attribute: {x[i]}')
        setattr(obj, x[i], '########')
    print(obj)

def fun_4(*objs):
    '''Create dataclass objects from a list of values'''
    print('=' * 40)
    x = len(objs)
    if x == 3:
        user = User(objs[0], objs[1], objs[2])
        print(user)
    elif x == 4:
        dog = Dog(objs[0], objs[1], objs[2], objs[3])
        print(dog)
    elif x == 5:
        plane = Plane(objs[0], objs[1], objs[2], objs[3], objs[4])
        print(plane)
    else:
        print('Invalid number of arguments')
