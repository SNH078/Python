class employee:
    salary=234  #base salary
    increment=20

    @property
    def salaryAfterInc(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterInc.setter
    def salaryAfterInc(self,salary):
        self.increment=((salary/self.salary)-1)*100


e=employee()

print(e.salaryAfterInc)
e.salaryAfterInc=455.8  # ((455.8 / 234 )-1 )* 100  => 94.78
# recalculates the increment when salaryAfterInc is manually set to 455.8
print(e.increment)
print(e.salary)
print(e.salaryAfterInc)
