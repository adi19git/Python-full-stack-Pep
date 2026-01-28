# print("hello world!")
# a=("Aditya")
# print(a)

# b=4
# print(b)
# print(type(b))

# c = 8.9
# print(c)
# print(type(c))

# d=True
# print(d)
# print(type(d))

# x=int(input("Enter your age\n"))
# if(x>=18):
#     print("You are eligible to vote")
# else:
#     print("you are minor")

# y=int(input("Enter a number\n"))
# if(y%2==0):
#     print("The number is Even")
# else:
#     print("The number is odd")    

# z=int(input("Enter the marks\n"))
# if(z>=90):
#     print("Grade= A")
# elif(z>=75):
#     print("Grade= B")
# elif(z>=50):
#     print("Grade= c")
# else:
#     print("Fail")     



# num1=int(input("Enter the 1st number\n"))
# num2=int(input("enter the 2nd number\n"))

# if(num1>num2):
#     print("greater number=" ,num1)

# elif(num1==num2):
#     print("both are equal")
# else:
#     print("The greater number is ", num2) 


# input=str(input("Enter the Color Input\n"))

# if(input=="red"):
#     print("You have to stop")
# elif(input=="yellow"):
#     print("Get ready to go")
# elif(input=="green"):
#     print("You can go")
# else:
#     print("Invalid input")    

# for i in range(1,15):
#     if(i % 2 !=0):
#         print(i) 
 
# for i in range(1,8):
#     print("*" *i)

# x = 3
# i = 1

# while i <= 10:
#     print(x, "x", i, "=", x * i)
#     i += 1


# def greet():
#     print("Hello")
# greet()

# a=int(input("Enter 1st num"))
# b=int(input("Enter 2nd num"))

# def sum(a,b):
#     print(a+b)
# sum(a,b)    

# def mul(a,b):
#     print(a*b)
# mul(a,b)    

# add=lambda x,y: x+y
# print(add(10,20))

# square=lambda x:x*x
# print(square(4))

# a=int(input("Enter the num"))
# print(a)
# print(type(a))
# print(2*a)

# salary="20000"
# converted=int(salary)
# print(type(converted))

# x=7
# i=1
# count=0

# while i<=10:
#     print(x, "X" ,i,"=",x*i)
#     i+=1
#     count+=1
# print("Count",count)

# num=12345
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print("Reversed number:", rev)

# cube= lambda x:x*x*x
# print(cube(5))

# marks = [10,20,30,0,50]
# print(marks)
# print(marks[3])

# marks.insert(1,75)
# print(marks)
# marks.append(80)

# marks.sort()
# print(marks)

# marks.remove(30)
# print(marks)

#lists

# city=["Delhi","Mumbai","Patna", "Motihari","Phagwara"]
# print(city)
# city.append("Goa")
# print(city)
# city.insert(2,"jalandhar")
# print(city)
# city.pop(2)
# print(city)
# city.sort()
# print(city)

# #touple
# frnds=('ansh','shivendra','mohit','yash','prashant','anish')
# print(frnds[1:4])
# print(len(frnds))
# print('mohit' in frnds)

#set
# numbers={10,20,30,40,50}
# #numbers.remove(20)
# numbers.discard(20)
# print(numbers)
# numbers.pop() #removes last element
# print(numbers)


# marks={70,84,66,70,91}
# marks.add(100)
# print(marks)
# marks.remove(70)
# print(marks)

#dictionary
# student={"name" : "Rahul" ,"age" : 21, "city" :"delhi" ,"course" : "python"}
# print(student)
# print(student["name"])
# print(student.get("age"))

# print(student.keys())
# print(student.values())
# print(student.items()) #print key and values together

# #student["age"]=22
# student.update({"age":32,"course" : "django"})
# print(student)

# print(student["age"])

# student.pop("city") #Removes and returns the last element of a list.
# student.popitem() #Removes and returns the element at a specific index.
# print(student)

# dict1={"a":2,"b" :3}
# dict2={"c":4,"d":5}
# print(dict1)

# dict1.update(dict2)
# print(dict1)

# mobile={"brand":"samsung","model" :"s24","price" : 75000,"stock" : 20}
# print(mobile)

# mobile.update({"stock":30})
# print(mobile)

# mobile.pop("price") #remove mentioned
# print(mobile)

# mobile.popitem() #remove last item
# print(mobile)


