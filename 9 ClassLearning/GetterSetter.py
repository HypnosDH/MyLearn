class Persion:
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age if age >= 0 else 0
    
    def __init__(self,name="",age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name:{} \n Age:{}".format(self.name, self.age)

if __name__ == "__main__":
    robert = Persion("Robert", 50)
    # print(robert.name, robert.age)
    print(robert)
    lisa = Persion("Lisa", -20) 
    # print(lisa.name, lisa.age)
    print(lisa)