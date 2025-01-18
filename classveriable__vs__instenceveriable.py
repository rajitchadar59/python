class e:
    companyname="apple"
    ne=0
    def __init__(self ,a):
        self.name=a
        self.raiseamount=0.02
        e.ne += 1
    def show(self):
        print(f"name of employee ->{self.name} and the raise amount in{self.ne} of sized {self.companyname} is->{self.raiseamount} ")

l=e("rajit")
l.raiseamount=3
l.companyname="appleindia"
l.show()    
# e.show(l)      

b=e("raj")

b.companyname="rohan company"
b.show()  
e.companyname="google"
print(e.companyname)