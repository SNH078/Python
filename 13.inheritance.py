# single
# multilevel (employe,programmer, manager)
# multiple (programmer->coder,employee)
class employee:
    company="ITC\n"
    def show(self):
        print(f"the name of employee is {self.name} and salary is {self.salary}")

class programmer(employee):
    company="ITC INFOTECH"
    def __int__(self):
      super().__init__()   #parent constructor also executed 
      print("prog const")

    def showLanguage(self):
        print(f"The name id {self.name} and he is good in {self.language} language ")

a=employee()
b=programmer()

print(a.company,b.company)