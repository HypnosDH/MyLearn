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

    def __eq__(self,other):
        if (self.name == other.name) and (self.age == other.age):
            return True
        else:
            return False

if __name__ == "__main__":
    robert1 = Persion("Robert", 50)
    robert2 = Persion("Robert", 50)
    print(robert1 == robert2)