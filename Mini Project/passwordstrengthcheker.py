import random
import string
import math
import os
import re
#generate password
password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$", k=10))
#check length
length = len(password)
#count characters using regex
letters = len(re.findall(r"[A-Za-z]", password))
digits = len(re.findall(r"[0-9]", password))
special = len(re.findall(r"[^A-Za-z0-9]", password))
#strength score
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
print("Saved to:", file_path)
