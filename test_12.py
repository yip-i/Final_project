



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

def password_strength(password):

    # There are sometimes invisible characters in text files. New line doesn't appear when you are looking at the text file
    # but every new line has one.
    password_read = open("password.txt", "r")

    # This is for Bijal who taught me about line comprehension

    common_passwords = [word.rstrip("\n") for word in password_read]


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


