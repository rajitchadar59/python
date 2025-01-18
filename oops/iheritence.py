class employee:
    def __init__(self ,name , id):
        self.name=name
        self.id=id

    def showdeatails(self):
        print(f"the name of employee:{self.id} is {self.name}") 


class programer(employee):
    def showlamguage(self):
        print("the default language is python")
    

e1= employee("rohandas" ,420)
e1.showdeatails()        
e2= programer("rajit" ,400)
e2.showdeatails() 
e2.showlamguage()


