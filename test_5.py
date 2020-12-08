


import os


"""
Try to open and read all lines of code from password.txt

"""



def main():
    list = []
    count = 0

    try:
        filename = "passwords.txt"

        if os.path.exists(filename):


            file = open(filename, "r")

            for line in file:
                list.append(line)
                count += 1

            print(list)

    except:
        pass





main()

