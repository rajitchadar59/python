class school:
    def __init__(self , nameo):
        self.sc=nameo
    def show(self):
        print(f"the name of school is :{self.sc}")
class rajit(school):
    def __init__(self, nameo , name):
        super().__init__(nameo) 
        self.name=name  
    def show(self):
        school.show(self)
        print(f"the name is : {self.name}")
class employee(rajit):
    def __init__(self, nameo, name):
        super().__init__(nameo, name) 

    def show(self):
        rajit.show(self)
        print("the deatails are given above ")

e=employee("saraswati shishu mandir rahatgrah (mp)" , "rajit chadar") 
print(e.show())                    