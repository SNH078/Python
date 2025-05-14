# list  -------------------------------------------------------------------------

# collection of mutable items
friends = ["apple", "rohan","akash",3,"f",5.3]
# list maintains the order giver by user
"""
friends[0]="harry"    #string's character are non-assignable but list elements are ! 
# friends[0][1]="g"    # modifying string . not possible
print(friends)
"""

#1 list function 
# R1:all the fns are directly applied on original list , no copy of list is created
# slicing 

print(friends[1:3])
friends.append("harry")
print(friends)

l1=[3,54,8,2,-1]
l1.sort()
l1.reverse()
l1.append(99)
l1.insert(3,0) #insert 0 at index 3 
x=l1.pop(2) # pop index 3 value 
print(x)
print(l1)


