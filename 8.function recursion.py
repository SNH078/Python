# function 
def car():
    a=int(input("enter a :"))
    b=int(input("enter b :"))
    c=int(input("enter c :"))

    average=(a+b+c)/3
    print(average)

car()

# recursion 
def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)

n=int(input("enter n : "))
print(f"factorial : {fact(n)}")


