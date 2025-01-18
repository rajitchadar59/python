class animal:
    def __init__(self , name , species):
        self.name= name
        self.species= species

    def make_sound(self):
        print("sound made by an animal")



class dog(animal):
    def __init__(self ,name , breed):
        self.breed = breed
        animal.__init__(self , name , species=dog)

        
    def make_sound(self):
        print("bark!")

d = dog("dog" , "doger man") 
d.make_sound()

a= animal("dog " , "dog")
a.make_sound()