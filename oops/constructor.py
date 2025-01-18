class Person:
    def __init__(self ,n ,o):
        print("hey i am a person")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is {self.occ}")


a= Person("rajit" ,"devloper")
b=Person("nikita" ,"Hr")
# c=Person() through erroe

a.info()
b.info()
# b=Person()
# a.name="nikita"
# a.occupation="my love"

# a.info()
