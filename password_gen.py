# Imports
import random


# Function to generate the passwords
def gen_pw(pw_length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = []  # List to store all the passwords

    for i in pw_length:

        password = ""  # Variable to store the generated password
        for j in range(i):
            j = random.randrange(len(alphabet)) #generate random from alphabet
            password = password + alphabet[j] #append password with j(random from alphabet)

        password = replaceWithNumber(password) # function where some characters are replaced with random number
        password = replaceWithUppercase(password) ## function where some characters are replaced with random Uppercase char

        passwords.append(password)  # Appending the generated password to the master list

    return passwords


# Function to replace 1 or 2 characters with a number
def replaceWithNumber(pword):
    for i in range(random.randrange(1, 3)):
        i = random.randrange(len(pword) // 2) 
        pword = pword[0:i] + str(random.randrange(10)) + pword[i + 1:]
        return pword


# Function to replace 1 or 2 letters with an uppercase letter
def replaceWithUppercase(pword):
    for i in range(random.randrange(1, 3)):
        i = random.randrange(len(pword) // 2, len(pword))
        pword = pword[0:i] + pword[i].upper() + pword[i + 1:]
        return pword


# main fuction
def main():
    numPasswords = int(input("How many passwords do you want to generate? "))

    print("System is about to generate {} passwords". format(str(numPasswords)))

    passwordLengths = []

    print("Enter the length of the passwords. Minumum Length = 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password:".format(str(i + 1))))
        if length < 3:
            length = 3
        passwordLengths.append(length)

    Password = gen_pw(passwordLengths)

    for i in range(numPasswords):
        print("Password # {} is {}".format(str(i + 1), Password[i]))


# run the code
main()