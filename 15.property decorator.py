#property decorator makes the function act like an attribute than a method 
#  if e=employee() is an object of class employee , we can print (e.name) to print the ename by internally calling name() function

class employee:
    a=1

    @classmethod
    def show(cls):
        print(f"the class value of a is {cls.a}")


    @property
    def name(self):
        # return self.ename
        return f"{self.fname} {self.lname}"
    

    # abstracton --hiding implmentation(below)
    @name.setter
    def name(self,value):
        # self.ename=value
        # jha space h vha split krdo
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
#There’s no strict requirement to split the name , ur choice


e=employee()
e.a=45

# e.name="harry"
e.name="harry khan kk"
print(e.name)
e.show()