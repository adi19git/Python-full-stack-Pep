#single inheritence
# class Parent:
#     def work(self):
#         print("I will go to work")
# class Child:
#     def work(self):
#         print("I will go to school")
# c1=Child()
# c1.work() #child class method will always override the parent class

#multiple inheritence


# class Father:
#     def eyes(self):
#         print("I have beautiful eyes")

# class Mother:
#     def voice(self):
#         print("I have melodious voice")

# class Child(Father, Mother):
#     def character(self):
#         Father.eyes(self)
#         Mother.voice(self)
#         print("Child: cooking")

# c1 = Child()
# c1.character()

# class Geo1:
#     def shape(self):
#         print("Circle")

# class Geo2(Geo1):
#     def shape(self):
#         super().shape()
#         print("Rectangle")

# s1 = Geo2()
# s1.shape()

# teacher prints teaches coder coding student both teacher and coidng

# class Teacher:
#     def teaching(self):
#         print("Teacher know how to teach")
# class Coder:
#     def coding(self):
#         print("Coder knows how to code")
# class Student(Teacher,Coder):
#     def all(self):
#         super().teaching()
#         super().coding()

# s1 = Student()
# s1.all()

# class School:
#     def __init__(self):
#         print("Name: Aditya")

# class Child(School):
#     def details(self):
#         super().__init__()   
#         print("Role: Student")


# c1 = Child()
# c1.details()


# class Parent:
#     def __init__(self):
#         self.__x=10
# class Child(Parent):
#     def show(self):
#         print(self.__x)
# obj=Child()
# obj.show()


# class Parent:
#     def __init__(self):
#         self.__x=10 #private variable
# class Child(Parent):
#     def show(self):
#         print(self.__x)
# obj=Child()
# obj.show() #show error


#protected variable can be accessed within the class or inherited class, not outside the class

# class Parent:
#     def __init__(self):
#         self._x=100 #protected variable
# class Child(Parent):
#     def show(self):
#         print(self._x)
# obj=Child()
# obj.show()

# class Person:
#     def __init__(self, name):   # constructor
#         self.__name = name      # private variable

#     def get_name(self):         # getter method
#         return self.__name


# class Child(Person):
#     def show_name(self):
#         print("Name:", self.get_name())  # using parent method


# c1 = Child("Aditya")
# c1.show_name()
# # --------------------------------------------------------------------------------------------------
# class Account:
#     def __init__(self, balance):     
#         self._balance = balance       # protected variable

#     def show_balance(self):
#         print("Balance:", self._balance)
# class SavingAccount(Account):
#     def add_money(self):
#         amount = int(input("Enter amount to add: "))
#         self._balance += amount       
#         self.show_balance()           
# a1 = SavingAccount(1000)
# a1.show_balance()
# a1.add_money()

#-------------------------------------------------------------------------------------------------------
#diamond problem

# class Grandfather:
#     def role(self):
#         print("I am  Grandfather")

# class Father(Grandfather):
#     def role(self):
#         print("I am Father")

# class Mother(Grandfather):
#     def role(self):
#         print("I am Mother")

# class Child(Father, Mother):
#     pass

# c=Child()
# c.role()
# #------------------------------------------------------------------------------------------------------
# #polymorphism

# class Animal:
#     def speak(self):
#         pass

# class Human(Animal):
#     def speak(self):
#         print("Human is speaking")

# class Baby(Animal):
#     def speak(self):
#         print("Baby is crying")

# class Dog(Animal):
#     def speak(self):
#         print("Dog is barking")


# h = Human()
# b = Baby()
# d = Dog()

# h.speak()
# b.speak()
# d.speak()
# #--------------
# class Vehicle:
#     def move(self):
#         pass

# class Car(Vehicle):
#     def move(self):
#         print("Car is moving")

# class Truck(Vehicle):
#     def move(self):
#         print("Truck is moving")

# class Bike(Vehicle):
#     def move(self):
#         print("Bike is moving")


# c = Car()
# t = Truck()
# b = Bike()

# c.move()
# t.move()
# b.move()



# #--------
# class Person:
#     def role(self):
#         print("i am a person")

# class Student(Person):
#     def role(self):
#         print("i am a student")

# class Teacher(Person):
#     def role(self):
#         print("i m a teacher")
# class Assistant(Student,Teacher):
#     def role(self):
#         print("I am the assistant")

# s = Student()
# t = Teacher()

# s.role()
# t.role()



a=[1,2,3,4]
b=a
b.append(5)
print(a)
