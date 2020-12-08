

import time

"""
Iphone, 4 number password guesser

"""

def iphone_password_guess(password):
    start_time = time.time()
    print(start_time)
    for first in range (10):
        for second in range(10):
            for third in range(10):
                for fourth in range(10):
                    guess_password = str(first) + str(second) + str(third) + str(fourth)
                    if guess_password == password:
                        end_time = time.time()
                        print(end_time-start_time)

                        return guess_password


def iphone_password_guess6(password):
    start_time = time.time()
    print(start_time)
    for first in range (10):
        for second in range(10):
            for third in range(10):
                for fourth in range(10):
                    for fifth in range(10):
                        for sixth in range(10):
                            guess_password = str(first) + str(second) + str(third) + str(fourth) + str(fifth) + str(sixth)
                            if guess_password == password:
                                end_time = time.time()
                                print(end_time-start_time)

                                return guess_password




def main():
    x = iphone_password_guess("6230")
    print(x)

    y = iphone_password_guess6(("623040"))



main()