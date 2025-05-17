# while ------------------------------------
i=1 
while(i<6):
    print(i)
    i+=1
    
print("\n")

# for ------------------------------------
for i in range(4):  #can use for with string , tuple , list 
    print(i)

print("\n")

#  range() function ------------------------------------
for i in range(3,8):
    print(i)
else:
    print("done")  #this is printed when the loop exhaust

print("\n")

# break ,continue------------------------------------
for i in range(6):
    if(i==4):
        break
    print(i)
print("\n")

#  pass ------------------------------------
for i in range(30):
    pass
for i in range(3):
    print(i)
print("\n")

# star pattern ----------------------------------------------------------------
"""
    *
  * * *
* * * * *
"""

n=int(input("enter n : "))
for i in range(1,n+1):
    print(" "*(n-i),end="") # print function ends with a newline.Passing the whitespace to the end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a newline.
    print("*"*(2*i-1),end="")
    print("\n")

#