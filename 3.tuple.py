# tuple collection of immutable items 
# string is immutable , list is mutable 
# tuple  maintains order given by user
a= (1,3,"car",3,99,False ,"harry",4.56,None,True)
print(a)

# way of writing (confusion)
"""
# a=(1) #python will consider this as a int ..
a=(1,) # now okay , tuple  
print(type(a))
"""

#  Immutable 
"""
print(a[3])
# a[0]=23    # non-assignable 
# print (a[0]) (error)
# a[3][2]="gg"  # non -assignable (error)
print(a)
"""

# function application results in copy of tuple 
# same as string , but changes in list are done on original list 

print(a.count(3)) # counts  frequency
print(3 in a) #check presence 
print(a.index("car")) # index of car 
b=(0,"boy")   # another tuple b defined 
print(a+b) # concatenation
print(len(a+b)) # len
print(a)

