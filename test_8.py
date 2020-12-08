
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
        print("1. Check password strength")
        print("2. Write a shift encrypted text file")
        print("3. Open shift encrypted text file")
        print("q. Quit")

        choice = input("Enter choice here: ")

        # Two different options will read the password file and pull on it for information.
        # If I initialize it now, it will take an extra if statement later, but skip reading the file again
        common_passwords = []

        if choice == "1":

            # There are sometimes invisible characters in text files. New line doesn't appear when you are looking at the text file
            # but every new line has one.

            password = input("Enter your password: ")

            if len(common_passwords) < 2:
                password_read = open("password.txt", "r")

                # This is for Bijal who taught me about line comprehension

                common_passwords = [word.rstrip("\n") for word in password_read]

            password_strength(password,common_passwords)

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
                pass

            else:
                file_write = open("Decrypted.txt", "w")
                file_write.write(x)
                file_write.close()

        else:
            print(f"No menu choice chosen. {choice} is not valid. Please enter something from the menu options.")




"""
Imports my password class.
The password class contains functions to check length and character composition.
"""
from Password import Password


"""
Function: password strength
parameters: the password and a list of the 1000 most common passwords
Returns: None. But will print out several different statements.
Will check the length, characters and assign a score on how it computes.
"""

def password_strength(password, common_passwords):
    if password in common_passwords:
        print("Your password is garbage.")
        # Thanks Carey for showing me f in front of string
        print(f"Your password is number {common_passwords.index(password)} in a list of most common passwords.")

    else:
        the_password = Password(password)
        password_score = 0

        password_length = the_password.get_length()

        if password_length < 5:
            password_score -= 100
        elif  5 <= password_length <= 10:
            password_score += 10
        elif password_length > 10:
            password_score += 20

        if the_password.contain_capital():
            password_score += 5

        if the_password.contain_lower_case():
            password_score += 5

        if the_password.contain_number():
            password_score += 5
        if the_password.contain_symbol():
            password_score +=5

        print(f"Your password scored {password_score}/40")



def main():

    menu()
    print("Endgame")

main()