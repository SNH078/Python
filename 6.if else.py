a=int(input("enter your age : "))

if(a>=18):
    print("you are abve 18") # notice the automatic indent here 
elif(a<0):
    print("invalid")
   
else:
    print("not 18 or more")
print(a) #out of scope --no indents