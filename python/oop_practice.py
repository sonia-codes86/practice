from itertools import product


class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def info(self):
        return f"{self.name} : {self.grade}"

stu1=Student("sonia",20)
stu2=Student("mehdi",28)
print(stu1.info())
print(stu2.info())

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def apply_discount(self,precent):
        self.price=self.price-self.price*precent/100
        return f"{self.name} price with discount {self.price}"

pro1=Product("lipstack",150000)
print(pro1.apply_discount(20))

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
p1=BankAccount(100000)
p2=BankAccount(250000)
print(p1.deposit(20000))
print(p2.withdraw(30000))



class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,title):
        self.books.append(title)
    def show_books(self):
        for i,title in enumerate(self.books, start=1):
            print(i,title)
    def remove_book(self,title):
        if title in self.books:
            self.books.remove(title)
        else:
            print("book not found")

    def count_books(self):
        return len(self.books)
lib=Library()
lib2=Library()
lib.add_book("bnavayan")
lib.add_book("james")
lib.add_book("shab")
lib.show_books()
lib2.add_book("tanhaee")
lib2.add_book("toty")
lib2.show_books()
print(lib2.count_books())
print(lib.count_books())