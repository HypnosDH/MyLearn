from RedefOperator import Persion

class SalaryException(Exception):
    def __init__(self, raise_rate):
        self.raise_rate = raise_rate

    def __str__(self):
        return "薪水調整過高：{:%}".format(self.raise_rate)

class Employee(Persion):
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary if salary >= 23100 else 23100

    def __init__(self, name="", age=0, salary=0):
        super().__init__(name, age)
        self.salary = salary
    
    def __str__(self):
        return super().__str__() + "\nSalary:{}".format(self.salary)

    def raiseSalary(self, newSalary):
        raise_rate = (newSalary - self.salary) / self.salary
        if raise_rate <= 0.05:
            self.salary = newSalary
        else:
            raise SalaryException(raise_rate)

if __name__ == "__main__":
    robert = Employee("Robert", 26, 19600)
    print(robert)

    try:
        robert.raiseSalary(42000)
    except SalaryException as ex:
        print(ex)

        
