class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        return f"{self.name}, {self.age} years old"

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade

    def info(self):
        return f"{super().info()}, grade:{self.grade}"

s=Student("sonia",19,20)
print(s.info())
print(s.name)

class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return "...."

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        return "Meow!"

d=Dog("koko")
print(d.speak())
c=Cat("jodis")
print(c.speak())

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


class Manager(Employee):
    def __init__(self,name,salary,bouns):
        super().__init__(name,salary)
        self.bouns=bouns

    def total_salary(self):
        total=self.salary+self.bouns
        return total

m=Manager("sonia",80000000,2000000)
print(m.total_salary())

d1=Dog("moka")
c1=Cat("jodis")
d2=Dog("koko")
c2=Cat("lili")
animals=[d1,c1,d2,c2]
for animal in animals:
    print(animal.name,":",animal.speak())

class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            return "not enough money"
        else:
            self.balance-=amount
            return self.balance
    def show(self):
        return f"Balance: {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self,balance):
        super().__init__(balance)

    def add_interest(self,percent):
        self.balance+=self.balance*percent/100
        return self.balance

acc=SavingsAccount(1000000)
print(acc.add_interest(10))
