#  lengthy -> 
l = [3,513,53,535]
index =0

for item in l:
    index+=1
    print(f"the item number {index} is {item}")

#  short -> 
for index,item in enumerate(l):
    print(f"item number at index {index} is {item}")

#  e.g.2 
l=[1,2,3,4,5,6,7,8]
for i ,item in enumerate(l):
    if i==2 or i==4 or i==6:
        print(item)