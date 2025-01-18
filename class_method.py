class employee:
    company="apple"
    def show(self):
        print(f"the name is {self.name} and a company is {self.company} ")


    @classmethod
    def changecompany(cls ,newcompany):
        cls.company=newcompany

e1= employee()
e1.name="rajit"
e1.show()
e1.changecompany("tesla")
e1.show()
print(employee.company)