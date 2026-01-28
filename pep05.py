# #object oriented programming
# class Student: #class name starts always with capital letter
    
#     print("Hey this is first class")

# s1=Student()
# print(s1) #prints class name , memory address 

#constructed is automatically called when object is created
#default constructor
# class Student:
#     def __init__(self):
#         self.name="Rahul"
#         print("This is our constructor")

# s1=Student()
# print(s1.name)


#parametrised constructor
# class Student:
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
# s1=Student("Avinash",40)

# print(s1.name)
# print(s1.marks)


# class Car:
    
#     def __init__(self,ModelNumber,Color):
#         self.model=ModelNumber #self.name is an atributes
#         self.colour=Color
# s1=Car(12413688,"BLUE")
# print("Model Number is ",s1.model)
# print("Color is",s1.colour)

#two types of attribute :class and object attributes


# class Student:
#     college_name="LPU"
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
# s1=Student("Rupesh", 90)
# s2=Student("Akash", 95)

# print(s1.name)
# print(s2.name)#object attribute

# print(s1.college_name)
# print(s2.college_name) #class attribute


# class Employee:
#     company_name="IBM"
#     def __init__(self, companyname, salary):
#         self.name=companyname
#         self.salary=salary
# e1=Employee("Aditya",50000)
# e2=Employee("Ankit",32000)

# print(e1.name)
# print(e2.salary)

# print(e1.company_name)
# print(e2.company_name)

# class Car:
#     showroom_name="DATSUN"
#     def __init__(self,model,color):
#         self.name=model
#         self.color=color
# c1=Car("SCORPIO","BULE")
# c2=Car("G WAGON"," WHITE")

# print(c1.name)
# print(c2.name)

# print(c1.showroom_name)
# print(c2.showroom_name)

# class Student:
#     college_name="LPU"
#     def __init__(self, student_name, marks):
#         self.name=student_name
#         self.marks=marks
# s1=Student("Aditya Kumar",57)
# s2=Student("Mohit",41)

# print(s1.name)
# print(s1.marks)

# print(s1.college_name)
# print(s2.college_name)

# s1.college_name="XYZ COLLEGE"
# s2.college_name="IIt Phagwara"

# print(s1.college_name)
# print(s2.college_name)


# class Employee:
#     company_name="GOOGLE"
#     def __init__(self, Employee_name, salary):
#         self.name=Employee_name
#         self.salary=salary
# s1=Employee("Aditya Kumar",57000)
# s2=Employee("Mohit",41000)

# print(s1.name)
# print(s1.salary)

# print(s1.company_name)
# print(s2.company_name)

# s1.salary=500000
# print(s1.salary)  #updated salary

#create a class student where, total student is a class attribut , and 
#and we have to increate the count whenever object is created

# class Student:
#     total_student = 0
#     def __init__(self,student_name,marks): #self represents current object
#         self.name=student_name
#         self.marks=marks
#         Student.total_student+=1

# s1=Student("Aditya Kumar",90)
# s2=Student("Mohit",1000)

# print(Student.total_student)

#methods / functions releted to object

# class Student:
#     def __init__(self,name):
#         self.name=name
#     def hello(self):
#         print("Welocme",self.name)
# s1=Student("Karan")
# s1.hello()


#static method
#we do not need to use self when staticmethod is used
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def hello(self):
#         print("Welcome", self.name)

#     @staticmethod
#     def college_name():
#         print("This is LPU")


# s1 = Student("Aditya")
# s1.hello()

# Student.college_name()   
# s1.college_name()        


#create a class student such that name , marks = object attributes,
#it has a normal method display method , it has to print hi "name Your marks is "marks"

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def Display(self):
#         print("hi",self.name,"Your marks is ",self.marks)
# s1=Student("Aditya",90)
# s2=Student("Mohit",80)

# s1.Display()


#make a class student , the normal method are show name , marks and static method is college name
#normal method is for object and static method is for class
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def show(self):
#         print("name is: ", self.name)
#         print("Marks is :", self.marks)
#     @staticmethod
#     def college_name():
#         print("This is LPU")
# s1=Student("Prashant jha2",20)
# s2=Student("Ankit",40)

# s1.show()
# s2.show()
# Student.college_name()
    

#encapsulation
# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
# s1=Student(40)
# print(s1.__marks)

# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
    
# s1=Student(40)
# print(s1.get_marks())

# class BankBalance:
#     def __init__(self, money):
#         self.__money = money

#     def get_balance(self):
#         return self.__money

#     def set_balance(self, new_balance):
#         self.__money = new_balance

# b1 = BankBalance(10000)
# b1.set_balance(29999)
# print(b1.get_balance())

#create a class bank balance where balance is hidden then deposit withdraw methods are used to access and modify the balance
# class BankBalance:
#     def __init__(self, balance):
#         self.__balance = balance   

#     def get_balance(self):
#         return self.__balance
    
#     def deposit(self, amount):
#         self.__balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient Balance")

# b1=BankBalance(100000)
# b1.deposit(20000)
# b1.withdraw(20000)
# print("Current Balance: ",b1.get_balance())

class Human:
    def eat(self):
        print("Human can eat")
class Student(Human):
    def study(self):
        print("Student can study")
s1=Student()
s1.eat()
s1.study()

class Animal:
    def speak(self):
        print("Animal can speak")
class Dog(Animal):
    def bark(self):
        print("Only dog can bark")

a1=Dog()
a1.speak()
a1.bark()