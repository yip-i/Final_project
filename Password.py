
"""
"""

"""
Class: Password
Has various functions to see if it contains a certain character.

"""
class Password:

    def __init__(self,password):
        self.password = password


    #Gets length of the object
    def get_length(self):

        return len(self.password)

    #Checks if the object contains a capital
    def contain_capital(self):
        for i in range(ord("A"), ord("Z") ):
            if chr(i) in self.password:
                return True

        return False

    #Checks if the object contains a lowercase
    def contain_lower_case(self):
        for i in range(ord("a"), ord("z")):
            if chr(i) in self.password:
                return True

        return False

    #Checks if the object contains a number
    def contain_number(self):
        for i in range(ord("0"), ord("9")):
            if chr(i) in self.password:
                return True

        return False

    #Checks if the object contains a symbol
    def contain_symbol(self):
        for i in range(ord("!"), ord("/")):
            if chr(i) in self.password:
                return True

        #There are a second batch of characters in python.
        for i in range(ord(":"), ord("@")):
            if chr(i) in self.password:
                return True



        return False



    # def get_password_score(self):
    #
    #     score = 0
    #     if self.password.contain_capital():
    #         score += 1
    #
    #     else:
    #         score = 0
    #
    #     return score



