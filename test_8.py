
"""
Menu system driving my whole program
"""

"""
No parameters in my menu function.
Acting as a driver for the rest of my program. A menu system

"""
def menu():

    choice = "x"
    while choice != "q":

        print("What would you like to do?")
        print("1 = Check password strength")
        print("2 = Write a shift encrypted text file")
        print("3 = Open shift encrypted text file")
        print("q = Quit")

        choice = input("Enter choice here: ")

        # Two different options will read the password file and pull on it for information.
        # If I initialize it now, it will take an extra if statement later, but skip reading the file again
        common_passwords = []

        from test_12 import password_strength
        if choice == "1":



            password = input("Enter your password: ")
            password_strength(password)

        elif choice == "2":
            from test_9 import formatting

            file_write = open("Encrypted.txt","w")
            shift = int(input("What would you like your shift to be? \n"))

            sentence = ""
            output = ""
            while sentence != "q":

                print("Enter text. If you would like to quit, enter q.")
                sentence = input()
                if sentence != "q":
                    output += sentence + "\n"

            output = output.upper()

            # print(formatting(output,shift))
            file_write = open("Encrypted.txt","w")
            file_write.write(output)
            file_write.close()


        elif choice == "3":
            from test_9 import shift_cipher
            x = shift_cipher()

            if x == None:
                print("No shift found.")
                pass

            else:
                file_write = open("Decrypted.txt", "w")
                file_write.write(x)
                file_write.close()

        elif choice == "q":
            pass

        else:
            print(f"No menu choice chosen. {choice} is not valid. Please enter something from the menu options.")





def main():

    menu()
    print("Endgame")

main()