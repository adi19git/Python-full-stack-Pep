# contact = {}

# while True:
#     print("\n....... Contact Book ........")
#     print("1. Add contact")
#     print("2. View contacts")
#     print("3. Search contact")
#     print("4. Delete contact")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         name = input("Enter name: ")
#         phone = input("Enter phone number: ")
#         contact[name] = phone
#         print("Contact successfully added")

#     elif choice == '2':
#         if contact:
#             print("\nSaved contacts:")
#             for name, phone in contact.items():
#                 print(name, ":", phone)
#         else:
#             print("No contact found")

#     elif choice == '3':
#         name = input("Enter the name to search: ")
#         if name in contact:
#             print("Phone number:", contact[name])
#         else:
#             print("Contact not found")

#     elif choice == '4':
#         name = input("Enter the name to delete: ")
#         if name in contact:
#             del contact[name]
#             print("Contact deleted successfully")
#         else:
#             print("Contact not found")

#     elif choice == '5':
#         print("Exiting Contact Book...")
#         break   

#     else:
#         print("Invalid choice")

#studentlist = {}

# while True:
#     print("\n..... List of Students .....")
#     print("1. Add student details")
#     print("2. View list")
#     print("3. Search student")
#     print("4. Delete details")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         name = input("Enter the name: ")
#         course = input("Enter the course: ")
#         section = input("Enter the section: ")

#         studentlist[name] = {"course": course, "section": section}
#         print("Student details added successfully")

#     elif choice == '2':
#         if studentlist:
#             print("\nStudent List:")
#             for name, details in studentlist.items():
#                 print("Name:", name)
#                 print("Course:", details["course"])
#                 print("Section:", details["section"])
#         else:
#             print("No students found")

#     elif choice == '3':
#         name = input("Enter name to search: ")
#         if name in studentlist:
#             details = studentlist[name]
#             print("Name:", name)
#             print("Course:", details["course"])
#             print("Section:", details["section"])
#         else:
#             print("Student not found")

#     elif choice == '4':
#         name = input("Enter name to delete: ")
#         if name in studentlist:
#             del studentlist[name]
#             print("Student deleted successfully")
#         else:
#             print("Student not found")

#     elif choice == '5':
#         print("Exiting ...thankyou for using student record system")
#         break   

#     else:
#         print("Invalid choice")

#string manipulation
# a="javaaa programinggg"
# print(len(a))
# print(a[-1]) #print last alphabet
# print(a[:4])
# print(a.upper())
# print(a.lower())
# print(a.strip()) #remove spaces from start and end
# print(a.replace("javaaa","python"))
# print(a.find("o"))
# word=a.split()
# print(word)
# print(a.count('g'))

# b="abc"
# print(b.isalpha())
# print(b.isdigit())
# c="124"
# print(c.isalpha())
# print(c.isdigit())

# print(a.startswith('ava'))
# print(a[::-1]) #it reverses the string

# s="madam"
# if(s==s[::-1]):
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")


# #count alphabet frequency
# c="apple"
# for ch in c:
#     print(ch,":",s.count(ch))

# d="python"
# result=""
# for ch in d:
#     if ch in "aeiou":
#         result+="*"
#     else:
#         result+=ch
# print(result)

#file handling
