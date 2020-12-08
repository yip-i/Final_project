



import time



def four_letter_password_guess(password):
    start_time = time.time()
    print(start_time)

    for first in range (48,122):
        for second in range(48,122):
            for third in range(48, 122):
                for fourth in range(48,122):
                    guess_password = str(chr(first)) + str(chr(second)) + str(chr(third)) + str(chr(fourth))
                    if guess_password == password:
                        end_time = time.time()
                        print(end_time)

                        print(end_time - start_time)
                        return guess_password




def main():
    x = four_letter_password_guess("Zara")
    print(x)



main()