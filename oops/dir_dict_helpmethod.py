#dir() method
# x= [1,2,3]
# print(dir(x))
# print(x.sort())

#__dict__
# class person:
#     def __init__(self ,name , age ):
#         self.name=name
#         self.age=age
#         self.version=1
# p=person("rajit" ,20)
# print(p.__dict__)        


# help() method
class person:
    def __init__(self ,name , age ):
        self.name=name
        self.age=age
        self.version=1
p=person("rajit" ,20)
print(p.__dict__) 
print(help(person))