class employee():
    
    salary=900
    increment=9
    @property
    def salaryafterincrement(self):
        return f"{self.salary+(self.salary*self.increment)/100}"
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment= (self.salary*self.increment)/100

a=employee()
print(a.salaryafterincrement)
a.salaryafterincrement=90000
print(a.increment)



