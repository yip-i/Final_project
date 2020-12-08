

"""


"""


"""
https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb


"""

import time
import threading

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

def main():

main()
