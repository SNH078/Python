# Python Magic methods are the methods starting and ending with double underscores ‘__’. 
# Dunder methods = “Double Under (Underscores)”.


class employee: 
    language = "English"  # class attribute - attribute that belongs to a class
    salary = 1200000

# __inti__ : constructor
# takes self argument nd can take other aRGUMENTS TOO
# can write somthing else instead of self ..but it is a good practice to write the conventinally used word
    def __init__(self, name=None, salary=None, language=None):  # constructor
        if name is not None:
            self.name = name
        if salary is not None:
            self.salary = salary
        if language is not None:
            self.language = language
        print("I am creating object")
    
    def getinfo(self):
        print(f"language is {self.language}")

    def greet(self):
        print("good morning")
    # static function
    @staticmethod
    def say():
        print("GOOD")

# Creating an employee object without arguments
harry = employee()
harry.language = "cpp"  # instance(object) attribute
harry.name = "Harry"
harry.getinfo()
employee.getinfo(harry)  # gives same output
harry.greet()
harry.say()
#  or employee.say()
print(harry.name, harry.language, harry.salary)

# Creating an employee object with arguments
rohan = employee("rohan", 1000, "java")
print(rohan.name, rohan.language)