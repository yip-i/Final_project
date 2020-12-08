








def main():

    sentence = "Hello, how are you doing."
    split = sentence.split()

    print(split)
    lst = []
    for word in split:
        lst.append(word.rstrip(","))

    print(lst)



main()