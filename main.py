import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation
passLength = int(input("Enter the length of your Password : "))

# password = ""
# for i in range(passLength):
#     password = password + random.choice(charValues)

# print(f"Your random password is {password}")

#alternativ (LIST COMPREHENSION)
res = "".join([random.choice(charValues) for i in range(passLength)] )
print(res)
