class Persion:
    def __init__(self,name="",age=0):
        self.__name = name
        self.__age = age if age >= 0 else 0

    def getData(self):
        return (self.__name, self.__age)

if __name__ == "__main__":
    robert = Persion("Robert", -48)
    n1, a1 = robert.getData()
    print(n1, a1)
 