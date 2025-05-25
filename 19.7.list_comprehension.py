myList = [1,2,9,5,3,5]

# lengthy ->

# squaredList = []
# for item in myList :
#     squaredList.append(item*item)

# short -> 
squaredList=[i*i for i in myList]
print(squaredList)

# print talble
n=int(input("enter a number: "))
table =[n*i for i in range(1,11)]
print(table)
# NOW STORE THIS table in file.
with open ("tables.txt","a") as f:
    # f.write(str(table)+"\n")
      f.write(f"{str(table)}\n")     