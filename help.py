class employee:
    def __init__(self , name):
        self.name=name
    
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __str__(self):
        return(f"the name of the employee is {self.name} str")
    # def __repr__(self):
    #     return(f" employee is ('{self.name}')  ")
    def __call__(self):
        print("hey i am call")