


import time



def number_combinations():
    start_time = time.time()
    print(start_time)
    count = 0
    for first in range (10):
        for second in range(10):
            for third in range(10):
                for fourth in range(26):
                    for fifth in range(26):
                        for sixth in range(26):
                            count += 1
    print(count)



def main():
    number_combinations()




main()