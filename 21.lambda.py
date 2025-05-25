#  lambda arguements : expressions 

square =lambda x:x*x
print(square(6))

sum=lambda a,b,c:a+b+c
print(sum(1,2,3))


# join method (strings )
a=["harry","rohan","shubham"]

final="-".join(a)
print(final)

#  e.g. 2 
table =[str(7*i) for i in range(1,6)]
s="\n".join(table)
print(s)

# format method (strings)
a="{} is a good {}".format("harry","boy")
print(a)

# map 
l=[1,2,3,4]
sqr= lambda x:x*x
sqList=map(sqr,l)
print(list(sqList))

# filter 
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

# reduce
from functools import reduce
def sum(a,b):
    return a+b

mul = lambda x,y:x*y

print(reduce(sum,l))
print(reduce(mul,l))
