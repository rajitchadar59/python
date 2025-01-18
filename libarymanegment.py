class libarary:
    def __init__(self):
        self.nob=0
        self.books=[]

    def addbook(self ,book):
        self.books.append(book)  
        self.nob=len(self.books)

    def showinfo(self):
        print(f"the books has {self.nob} books the books are")
        for book in self.books:
            print(f"{book}")


l1=libarary()
l1.addbook("harry potter") 
l1.addbook("harry potter 1")   
l1.addbook("harry potter 2") 
l1.showinfo()    
        



        