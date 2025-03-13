# Module Imports
from types import *
import pandas as pd
import numpy as np
from collections.abc import Iterable


#Igual o no igual a [valor]
assert 5 == 5 # Success Example
assert 5 == 3 # Fail Example

assert 5 != 3 # Success Example
assert 5 != 5 # Fail Example

#type() is [valor]
assert type(5) is int # Success Example
assert type(5) is not int # Fail Example


#isinstance
assert type(5) is int # Success Example
assert type(5) is not int # Fail Example

#is [Tipo booleano]
true = 5==5
assert true is True # Success Example
assert true is False # Fail Example

#in y not in [iterable]
list_one=[1,3,5,6]
assert 5 in list_one # Success Example
assert 5 not in list_one # Fail Example

#Mayor o menor que [valor]
assert 5 > 4 # Success Example
assert 5 > 7 # Fail Example

# El módulo % es igual a [valor]
assert 2 % 2 == 0 # Success Example
assert 2 % 2 == 1 # Fail Example


#declaracion de afirmación any()
example = [5,3,1,6,6]
booleans = [False, False,True, False]
any(example)
any(booleans)
assert any(example) == True # Success Example
assert any(booleans) == True # Success Example

#declaracion de afirmación all()
assert all(example) # Success Example
assert all(booleans) # Fail Example


#Objetos personalizados
type(object).__name__
df = pd.DataFrame()
type(df).__name__
type(df).__name__ == 'DataFrame' # True Boolean
type(df).__name__ is 'DataFrame' # True Boolean
type(df).__name__ == type([]).__name__ #False Boolean
type(df).__name__ is type([]).__name__ #False Boolean
assert(type(df).__name__ == 'DataFrame') # Success Example
assert(type(df).__name__ == type([]).__name__) # Fail Example


#Iterables
from collections.abc import Iterable
iterable_item = [3,6,4,2,1]
isinstance(iterable_item, Iterable)
isinstance(5, Iterable)
assert isinstance(iterable_item, Iterable) # Success Example
assert isinstance(3, Iterable) # Fail Example


#Or/and
true_statement = 5 == 5 and 10 == 10
false_statement = 5 == 3 and 10 == 2
print(true_statement, false_statement)
assert true_statement # Success Example
assert false_statement # Fail Example

true_or_statement = 5 == 5 or 3 == 3
false_or_statement = 7 == 3 or 10 == 1
print(true_or_statement, false_or_statement)
assert true_or_statement # Success Example
assert false_or_statement # Fail Example


#
class Test(object):
    def __init__(self, first_name, last_name ):
        self.first_name = first_name
        self.last_name = last_name
    def test_all_class_arguments(self):
        print('Testing both of the class variables to see whether they are both strings!')
        for _ in [self.first_name, self.last_name]:
            assert(type(_) is str)
            print('------')
            print('Passed all of the tests')
yay = Test('James' , 'Phoenix') # Success Example
yay.test_all_class_arguments()

yay = Test(5 , 'Phoenix') # Fail Example
yay.test_all_class_arguments()


class Example():
    def __init__(self, id_, name):
        self._id = id_
        self.name = name
    def subtract(self):
        answer = 5 + 5
        return answer
    def test_lambda_function(self):
        assert(lambda x: x is LambdaType)
    def test_subtract_function(self):
        assert(self.subtract is LambdaType)
example_class = Example("123", 'James Phoenix')
print(example_class._id, example_class.name)

example_class.test_lambda_function() #Success Example
example_class.test_subtract_function() #Fail Example

