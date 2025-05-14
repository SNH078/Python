# 1 PIP package installer in python-------------------------------------------------------
"""
import pyjokes
print("printing jokes ...")
joke = pyjokes.get_joke()
print(joke)
"""
#2 REPL - read evaluate print log(windows+right ->terminal ..write python ..5+3)-------------------------------------------------------
#3 pyttsx (text to speech )-------------------------------------------------------
"""
import pyttsx3
car = pyttsx3.init()
car.say("Hello India ..kya haal hai ..")
car.runAndWait()
 """

#4 print contents of directory using OS module -------------------------------------------------------
"""
import os 

#specify directory
directory_path='/drive'

#list all  file nd dir in specified path 
contents = os.listdir(directory_path)

# print each file nd dir name
for item in contents:
   print(item)
"""
#5  variable -------------------------------------------------------
"""
a=1  # int
b=3.4  # float 
name= "harry" #string
d =False #bool  F nd T  capital 
e= None # None ..a variable has nothing in it( N capital )

print(a+b)

"""
#6 operators - arithmetic /Asosgnment / comparison / logical -------------------------------------------------------
# 7 type function and typecasting using type()-------------------------------------------------------
"""
a=3.4
f="5.6"
print(type(f))
print(f)
# typecasting 
a=float(f)
print(a)
print(type(a))
"""

# 8 user input -------------------------------------------------------
"""
a =input("enter no.")
b =input("enter no.")
print ("no. is ", a+b, " u can write here also !") 
#  user inputs have string type

a =int(input("enter no."))
b =input("enter no.")
print ("no. is ", a+b) # concantenate  ..use type()
"""

#9 string-------------------------------------------------------
# strings are immutable ..we cannot change them ..strings are non-assignable ...once given a value
# three ways 
"""
a ="harry"
b='''hari'''
c='car'

# string slicing (strt from 0)(reverse start frm -1 from last)

name = "amazingG"
newname = name[0:3]   #end 3 is not included
nn2= name[-3:-1]       #end -1 is not included
nn3= name[1:3] 
nn4=name[1:] # till length
nn5=name[:3] # start from 0 

# skip in slice    start:end(not included):skip+1
nn6= name[1:6:3]
nn7= name[1::3] # print every 3rd in the sliced part

print(newname,nn2,nn3,nn4,nn5,nn6,nn7)

#can also write it this way
# name = "amazingG"
# print(name[0:3])

"""

# string function -------------------------------------------------------
"""
#R1:application of string fn on a string creates copy of string nd then applies the function

name="hArryR"
print(len("harry"))
print(name.endswith("rry"))
print(name.startswith("rry"))
print(name.capitalize())
print(name.upper())
print(name) # no change ...R1 
print(name.lower())
# find index of r
print(name.find("r"))
# replace all occurencs ..all capital small 
print(name.replace("r","T"))
"""

# 10. escape sequence character \n  \t  \"car\"  -------------------------------------------------------
"""
a="car is\nred \"in\" colour"
print(a ,"\n")

# Note : f-string
name= "harry"
print("Good afternoon, " + name) # old way
print(f"Good afternoon, {name}")
print("Good afternoon,",name) 

# Note - chaining 
letter='''Dear <|name|> you are selected <|date|>'''
print(letter.replace("<|name|>","harry").replace("<|date|>","23 dec 2024")) #replaced vli string me hi date replacemnet kro 
"""


# random integer 
import random
score=random.randint(1,45)
print(score)