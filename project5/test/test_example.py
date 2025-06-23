import pytest

def test_equal_or_not_equal():
    assert 3==3
    assert 3!=1
    
def test_is_instance():
    assert isinstance('this is string',str)
    assert isinstance('10',str)
    
def test_booleans():
    validate = True
    assert validate == True
    assert ('Hell Wrold'=='Hello') is not True
    
def test_greater_than_less_than():
    assert 4==4
    assert 7>4
    assert 4<7

def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False,False]
    assert 1 in num_list
    assert 7 not in num_list
    assert  all(num_list)  #check if all the value is truth(false value are 0,False etc)
    assert not any(any_list)  # check if atelast 1 value is truth
    
class Student:
    def __init__(self,first_name:str,last_name:str,major:str,years:int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

@pytest.fixture
def default_employee():
    return Student('John','Doe','Computer Science',3)

def test_person_initialization(default_employee):
    assert default_employee.first_name == 'John'
    assert default_employee.last_name == 'Doe'
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 3
        