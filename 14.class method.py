# class method decorator: used to create a class method 
#: method which is bound to class and not object of class
# class method is a way ... method k andr class ko access krne ka 
class employee:
    a=1


# shows class attribute and not instance attribute i.e. 45 when e.show is executed
# cls instead of self
# cls means class
 
    # @classmethod   # uncomment this to see how clss method works to display class values 
    def show(cls):
        print(f"the class value of a is {cls.a}")

e=employee()
e.a=45

e.show()