# dictonary
#  collection of key- value pair 
# Property : unordered , mutable(same as list) , indexed , no duplicate allowed( returns only one value..that is written at last ..(here , rohan 65)) 
# empty dictionary 
# functions are applied on original dictionary(like list)..NO copy is created
ram={}
print(ram)

marks ={
    "harry":99,
    "rohan": 34,
    "rohan": 65,   
    "shubham": 87,
    3 : 53.9,
    0 : "boy",
    4:False,
    "a":[1,6,8.7]
}

print(type(marks))
print(marks)
print(marks["harry"])
print(marks[4])
print(marks["a"])
print(marks["a"][2])


#  function
print("\nfunnn**********\n")

print("length :", len(marks))

print(marks.items())

print(marks.pop("harry"))  #removes key-"harry" and returns its value  ->99

print("------ ",marks)

print(marks.keys()) # returns ALL keys ...only left side
print(marks.values()) # returns ALL  values ...only right side

marks.update({"harry":100, "akash":45}) # old is updated , new is added 
print(marks)  

print(marks.get("harry")) # 
print(marks.get("arun65")) # returns None if key is not present
# print(marks["arun"]) #returns error if not present 

num=marks.copy() # gives shallow copy of dictionary
print(num)
print(num.clear()) # empties the dictionary
print(num) 

