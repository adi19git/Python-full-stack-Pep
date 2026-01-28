
# class Human:
#     def eat(self):
#         print("Human can eat")
# class Student(Human):
#     def study(self):
#         print("Student can study")
# s1=Student()
# s1.eat()
# s1.study()

# class Animal:
#     def speak(self):
#         print("Animal can speak")
# class Dog(Animal):
#     def bark(self):
#         print("Only dog can bark")

# a1=Dog()
# a1.speak()
# a1.bark()

#p class - nokia =only call, child- iphone call and internet

class Nokia:
    def fun1(self):
        print("Nokia can only makes call")
class Iphone(Nokia):
    def fun2(slef):
        print("Iphone can both make call and internet")

p1=Iphone()
p1.fun1()
p1.fun2()
