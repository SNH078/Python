# set 
# collection of non repeatable elements 
# Properties:  unordered, unindexed , immutable ,non-repeatable (unique)(like dictionary) 
#  set also uses {}  like dictionary 
# (unordered) set does not maintain the order giver by user..but list does
# function are applied on original set( same as list)  -- NO copy is created

s={1,"Harry",5,32,5,5,"32",False}
print(s,type(s)) #print s , its type

# empty set (***) different from  dictionary 
# as s={} will create an empty dictionary
e= set()
print(e)



# function 
print(len(s))
s.remove(5)
s.add(666)
s.pop() # deletes any random element ...use not preferred 
print(s)
s.clear()
print("NOTE th o/p : ", s)



# Maths ( set operation )
s1={1,3 ,67.6}
s2={3,8, 3.3,3} 
print(s1.union(s2))
print(s1.intersection(s2))
print(s2-s1)
print(s1-s2)
print(s1.difference(s2)) # s1-s2
print({3,67.6}.issubset(s1))
print({3,67.6}.issubset(s1))
print(s1)
s1.clear()
#  Note : we cannot have a list as an element in set ..s set require all its element to be hashable and immutable 
# list as not hashble nd mutable 
#  not possible  s={1 ,6 ,5 ,54 ,[2,"harry"] }

# conclusion 
"""
fn application result in copy creation - tuple 
imuutable : set , tuple  ,string
mutable  : dict , list 
assignable : list, dict ( updatek)
indexed : dict
unindexed : list , tuple , set
orderd : list , tuple ,dict
 unordered: set
 unique : dict, set 
  set dict : {}
  tuple : ()
  list []
  empty set :    car = set()
  empty dict :   car ={}
"""