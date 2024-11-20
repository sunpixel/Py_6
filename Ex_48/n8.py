# pylint:disable = C2801
'''The Data Class module'''

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

@dataclass(order=True)
class Plane:
    '''Reperesent an aircraft'''
    type: str
    age: int
    model: float
    capacity: int

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
    fun_1(aircraft1)

def fun_1(craft):
    '''Function 1'''
    x = list(map(lambda x: x, craft))
    print(x)
