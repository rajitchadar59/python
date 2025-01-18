 #THIS IS FOR CLASS METHOD 
# class perent:
#     def parent_method(self):
#         print("this is a parent method ")

# class child(perent):
#     # def parent_method(self):
#     #     print("child parent method()")
#     #     super().parent_method()
#     def child_method(self):
#         print('this is a child method')
#         super().parent_method()
# c=child()
# p=perent()
# # c.child_method()
# c.parent_method()


 #THIS IS FOR CONSTRUCTOR
class employe:
    def __init__(self , name , id):
        self.name= name
        self.id=id

class programmer(employe):
    def __init__(self, name, id , lang):
      super().__init__(name ,id)
      self.language=lang  

rohan = employe("rohan das" , "15")
harry=programmer("harry" ,"45" ,"python")
print(harry.name)
print(harry.id)
print(harry.language)

