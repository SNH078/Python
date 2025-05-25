# 1 -- Exception handling 

# python : try , except 
# c++ , JS : try ,catch
try:
    a = int(input("Hey, enter a number: "))  
    print(f"You entered: {a}")
except ValueError :
    # OR except ValueError as v: and then we can print v
    print("Invalid input! Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Thank you!")

# if we dont write this try catch then this thanku wont be printed in case of exception 

#  2 - raise : program crash hoga , except se crash nhi hota  ...bye print nhi hoga agr b=0 (crash)
a=int(input("enter number a : "))
b=int(input("enter number b : "))

if(b==0):
    raise ZeroDivisionError("dont divide by 0")
else:
    print(f"division a/b is  {a/b}")

print("bye !! ")



# 3- Try else   : else runs only when try is successeful
try:
    a = int(input("Hey, enter a number: "))  
    print(a)
except Exception as e:
   print(e)
else:
    print("I am inside else")

# 4 -finally : pass ya fail..dono case me finally ka code chlega 
try:
    a = int(input("Hey, enter a number: "))  
    print(a)
except Exception as e:
   print(e)
finally:
    print("I am inside finally")
