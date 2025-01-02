# innit is called creating constructor
class person: #class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self): #method
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome" +" " + self.firstname + " " + self.lastname +" "+ "to the class of" + " " + self.graduationyear )
x=student("Bola", "Ade", "2021")
x.welcome()

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x=person("Ayo", "Ade")
x.printname()