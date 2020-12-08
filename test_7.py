
import os
import zipfile

"""
Combining the code from test_5 which reads the most common passwords
with the code that tries to open a locked zipfile.

"""

secret_file = zipfile.ZipFile("top_secret.zip")

def open_locked_zip():


    filename = "Project/passwords.txt"
    file = open(filename, "r")
    count = 0
    possible_passwords = []
    for line in file:
        p = line.rstrip("\n")
        possible_passwords.append(p)

    for guess in possible_passwords:

        try:
            print(guess)
            secret_file.setpassword(str(guess).encode('ascii'))
            secret_file.extract("top_secret.txt")

            print("password found")
            break

        except:
            count += 1
            print(count)



def main():
    open_locked_zip()

main()