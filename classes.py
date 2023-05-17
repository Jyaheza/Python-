class myFirstClass:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def __str__(self):
        return ("Name is {self.name} and Age is {self.age}")
    def myFunc(self,country,city):
        self.country=country
        self.city=city
        print("And country is "+self.country+" and city is "+ self.city) 
obj1= myFirstClass("Maurice",22)
obj1.myFunc("Rwanda","Kigali")
#Inheritance 
class mySecondClass(myFirstClass):
    def __init__(self, name, age,address,hobby):
        super().__init__(name, age)
        self.address=address
        self.hobby=hobby
    def moreInfo(self):
        print("My Name is ",self.name," and my Age is ",self.age," and my address is ",self.address," And I like ",self.hobby)
obj2=mySecondClass("Maurice Irakoze",19,"2501 E Memoria Rd","Basketball")
obj2.moreInfo()
#tobe continued



