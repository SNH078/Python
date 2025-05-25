# walrus operator is used for "assignment within expressions" , reducing redundancy.

# Example: Without Walrus (:=)
"""
value = input("Enter name: ")
if len(value) > 3:
    print("Too long!")
"""

if(length := len(input("enter name : ")))>3:
    print(f"Too long {length}")


    # 2 - global vairavble 

a=68

def fun():
    a=3
    print(a)

fun()
print(a)