import json

class Book:
    def __init__(self,title,author,is_available=True):
        self.title=title
        self.author=author
        self.is_available=is_available

    def to_dict(self):
        return {"title":self.title,"author":self.author,"is_available":self.is_available}

    def __str__(self):
        status="available" if self.is_available else"borrowed"
        return f"{self.title} by {self.author} ({status})"

class Library:
    def __init__(self,filename="books.json"):
        self.filename=filename
        self.books=[]
        self.load()

    def load(self):
        try:
            with open(self.filename,"r",encoding="utf-8")as f:
                data=json.load(f)
                self.books=[Book(**item)for item in data]
        except FileNotFoundError:
            self.books=[]

    def save(self):
        with open(self.filename,"w",encoding="utf-8")as f:
            json.dump([b.to_dict()for b in self.books],f,ensure_ascii=False,indent=4)

    def add_book(self,title,author):
        self.books.append(Book(title, author))
        self.save()

    def show_books(self):
        for i,b in enumerate(self.books,start=1):
            print(i,b)

    def search_book(self,title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def find_book(self,title):
        for b in self.books:
            if b.title.lower()==title.lower():
                return b
        return None

    def borrow(self,title):
        book=self.find_book(title)
        if book is None:
            print("Book not found")
        elif not book.is_available:
            print("Book is already borrowed")
        else:
            book.is_available=False
            self.save()
            print("Book borrowed")


    def return_book(self,title):
        book=self.find_book(title)
        if book is None:
            print("Book not found")
        elif book.is_available:
            print("Book was not borrowed")
        else:
            book.is_available=True
            self.save()
            print("Book returned")

b1=Book("bnava","sadi",True)
print(b1)
lib=Library()
lib.show_books()
for b in lib.search_book("python"):
    print(b)

lib.borrow("bnava")
lib.borrow("bnava")
lib.show_books()
lib.return_book("bnava")
lib.borrow("xyz")

