import random #random module
import string #string module provides collection of constants

print("****RANDOM PASWORD GENEATOR****")

#user prompt to take input of desired passsword_length
password_length = int(input("Enter the password length: "))

#string variable that contains all letters,digits and punctuations
characters = string.ascii_letters + string.digits + string.punctuation

#initialised empty string to store random password generated
password = ""   

for index in range(password_length):
    
    #randomly chooses characters from character string
    password = password + random.choice(characters)

# Displays password
print(" Random Password generated: {}".format(password))
