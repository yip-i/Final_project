
def find_shift(list_strings, known_word):

    for i in list_strings:

        shift = ord(i[0]) - ord(known_word[0])

        if shift < 0:
            shift += 26

        if (ord(i[1]) - shift)  >= ord("A") and (ord(i[1]) - shift)  <= ord("Z"):

            if chr(ord(i[1]) - shift) == (known_word[1]):

                if change_word(i ,shift) == known_word:
                    return shift

        elif (ord(i[1]) - shift) < ord("A"):
            if chr(ord(i[1]) - shift + 26) == (known_word[1]):
                if change_word(i ,shift) == known_word:
                    return shift




def change_word(word, shift):
    string = ""



    for x in range(len(word)):
        if (ord(word[x]) - shift) >= ord("A") and (ord(word[x]) - shift) <= ord("Z"):
            string += chr(ord(word[x]) - shift)

        elif (ord(word[x]) - shift) > ord("Z"):
            string += chr(ord(word[x]) - shift - 26)

        else:
            string += chr(ord(word[x]) - shift + 26)


    return (string)

def main():
    lst = "BWGLE RM QCC FMU RFGQ MLC CLBQ"
    lst = lst.upper()
    lst = lst.split()
    print(find_shift(lst,"ENDS"))

main()