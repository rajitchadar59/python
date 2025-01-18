class Person:
    name="rajit"
    occupation="chadar"
    newworth=45
    def info(self):
        print(f"{self.name } is a {self.occupation}")
#objectt creation
a= Person()
b=Person()
a.name ="ram"
a.occupation="web devloper"
b.name ="nikita"
b.occupation="my gf"
# print(a.occupation)
# print(a.name)
a.info()
b.info()