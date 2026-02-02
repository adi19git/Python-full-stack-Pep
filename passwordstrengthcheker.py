import random
import string
import math
import os
# generate password
password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$", k=10))
# check length
length = len(password)
# count characters
letters = sum(c.isalpha() for c in password)
digits = sum(c.isdigit() for c in password)
special = length - letters - digits
# strength score 
score = math.ceil((letters + digits*2 + special*3) / length * 10)
# save using os
file_path = os.path.join(os.getcwd(), "passwordDetails.txt")
f = open(file_path, "w")

f.write("Password: " + password + "\n")
f.write("Length: " + str(length) + "\n")
f.write("Letters: " + str(letters) + "\n")
f.write("Digits: " + str(digits) + "\n")
f.write("Special: " + str(special) + "\n")
f.write("Strength Score (1-10): " + str(score) + "\n")
f.close()

print("Saved in:", file_path)
