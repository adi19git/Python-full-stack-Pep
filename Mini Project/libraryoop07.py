#implementation of 4 pillars of Oops in python
# Parent Class(ABSTRACTION)

class LibraryItem:
    def __init__(self):
        self.__charge = 0   # ENCAPSULATION 
    def calculate_charge(self, days):
        pass   
    def get_charge(self):
        return self.__charge
    def _set_charge(self, amount):
        self.__charge = amount
        
class Book(LibraryItem):   #INHERITANCE
    def calculate_charge(self, days):   # POLYMORPHISM
        charge = days * 10   
        self._set_charge(charge)

class Magazine(LibraryItem):
    def calculate_charge(self, days):   # POLYMORPHISM
        charge = days * 10   
        self._set_charge(charge)


# HAS-A Relationship
class LibraryApp:
    def borrow_item(self, item, days):
        item.calculate_charge(days)   

        print("Item Type:", item.__class__.__name__)
        print("Borrow Days:", days)
        print("Borrowing Charge:", item.get_charge())
        print()


book = Book()
magazine = Magazine()
app = LibraryApp()
app.borrow_item(book, 5)
app.borrow_item(magazine, 3)

