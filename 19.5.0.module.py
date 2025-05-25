# see 19.5main.py
def myFun():
    print("Hello world")

# myFun()
# print(__name__)   # module k iss code ko module vli file se hi run kiya h 

if __name__== "__main__":
    # if this code is directly executed by running the file its present in ..it will be executeed 
    # if u run main.py file where this fun () is imported then the beelow code wont be executed
    print("we are directly running this file")
    myFun()
    print(__name__)


#"If the module is being run directly from the command line, the 'name' is set to string 'main'. 
# Thus, this behaviour is used to check whether the module is run directly or imported to another file. 