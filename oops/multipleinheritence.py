class A:
    def __init__(self , name):
        self.name= name

    def show(self):
        print(f"the name is {self.name}")


class B:
     def __init__(self , dance):
        self.dance= dance

     def show(self):
        print(f"the dance is {self.dance}")
        

class c(A ,B):
    def __init__(self , dance , name):
        self.dance= dance
        self.name=name

o=c("kathak"  , "rajit") 
print(o.name)  
print(o.dance) 
o.show()
print(c.mro())
        
#mro() function ka use ye pata karne ke liye kiya jata hai ki function pehle kaha dhoondha jayega        
     