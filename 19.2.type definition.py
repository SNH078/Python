# Type definition refers to declaring the data type of a variable or function. 
# It helps in better code clarity, type checking, and optimization.

# type hint are added using : colon for variable
# and  -> for function return types 

# variable type hint
age:int=25
name:str ="Harry"

# function type hint
def greeting(name:str)->str:
    return f"Hello , {name} ! "


def sum(a:int,b:int):
    return a+b
# usage
print(greeting("Alice"))
print(sum(4,3))


# type hints 
from typing import List,Tuple,Dict,Union

numbers:List[int]=[1,2,3,4,5]
person:Tuple[str,int]=("Alice",30)
scores:Dict[str,int]={"Alice":90,"Bob":85}
identifier :Union[int,str]
identifier=12345 #also valid





