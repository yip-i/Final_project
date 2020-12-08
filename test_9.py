"""
Shift cipher decoder
If you know one word in the word,
you can decrypt the whole message.

"""
#actual_string
import os


"""
Find Shift.
Function
Find the shift of the words 
parameters: list of strings that are the same length as the known word and known word
Return: How much each character is shifted by

"""
def find_shift(list_strings, known_word):

    for i in list_strings:

        shift = ord(i[0]) - ord(known_word[0])

        if chr(ord(i[1]) - shift) == (known_word[1]):

            if change_word(i,shift) == known_word:
                return shift

"""
Module used to verify the shift by changing the word thought to be used for the shift

"""

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



"""
Find length of target word
parameters: strings, word that you know is in the sentence
return list of strings that are the same length as the word

"""


def same_length(sentence, known_word):
    known_length = len(known_word)
    same_length_words = []

    #Splits the text into a list
    list_words = sentence.split()

    # Turns it into a set to remove repeats
    list_words = set(list_words)

    #Remove commas and periods
    punctuation_removed = []
    for word in list_words:
        punctuation_removed.append(word.rstrip(",."))


    # Was originally just the list_words, but I changed it so that commas would be removed.

    for i in punctuation_removed:
        if len(i) == known_length:
            same_length_words.append(i)

    return(same_length_words)

"""
Translates the shifted cipher into regular text.
Parameters: The coded string of words and the shift of each character.
Return should be the string.
Warning: MUST BE UPPERCASE or translate module breaks.

"""

def translate(coded_string, shift):
    coded_list = coded_string
    string = ""

    for i in coded_list:

        for x in range(len(i)):

            # Special characters that are common, but are normally not shifted.
            # These include commas, quotation marks and semicolons
            if (i[x]) == "," or i[x] == "." or i[x] == ")" or i[x] == "(" or i[x] == "'" or i[x] == '"' or i[x] == "-" or i[x] == "?":
                string += i[x]

            elif (ord(i[x]) - shift) >= 65 and (ord(i[x]) - shift) <=90:
                string += chr(ord(i[x]) - shift)


            elif (ord(i[x]) - shift) < ord("A"):
                string += chr(ord(i[x]) - shift + 26)

            else:
                string += chr(ord(i[x]) - shift - 26)


        string += " "

    return (string)

"""
Handles the formatting for the rest of the program.
Pushes to the translate module to handle the translating.
Ensures if the new line character is present, it is added back in. 
Line split appears to remove the new line character. 

"""
def formatting(coded_string,shift):

    coded_list = coded_string.splitlines(keepends= True)
    output = ""
    for line in coded_list:
        # ensures that the new line character is added back into the code.
        if line.endswith("\n"):
            line = line.split()
            output += translate(line,shift) + "\n"
        #Handles for if there isn't a new line character. Normmally for the last line.
        else:
            line = line.split()
            output += translate(line,shift)
    return (output)



"""
Shift Cipher:
Opens
Drives the actions of the rest of the program

"""
from os import listdir
import os.path
from os.path import isfile, join

def shift_cipher():

    try:
        print("Here is a list of all files in the directory.")
        arr = os.listdir()
        print(arr)

        # file_name = input("Which one would you like to open? \n")
        file_name = input("Which file do you want to open? \n")

        #checks if file is type in correctly
        if os.path.exists(file_name):

            file_open = open(file_name,"r")

            file_string = ""
            for line in file_open:

                file_string += line
            # The translate module only works when everything is upper case.
            file_string = file_string.upper()

            file_open.close()


            print("1 = Don't know shift or word.")
            print("2 = Know a word. ")
            print("3 = Know the shift")
            decision = input("Input: ")
            # decision = "2"

            if decision == "1":
                output = ""
                for i in range(26):

                    output += (f"The shift is {i}. \n") + formatting(file_string,i) + "\n"

                return (output)

            elif decision == "2":

                try:
                    word_you_know = input("Word you know: ")

                    #program works better in uppercase
                    word_you_know = word_you_know.upper()

                    #Calls program same length to find all words of the same length

                    same_length_words = same_length(file_string, word_you_know)

                    shift = (find_shift(same_length_words,word_you_know))

                    if type(shift) == type(1):


                        output = ""
                        output += formatting(file_string,shift)
                        return output

                    else:
                        raise ValueError

                except ValueError:
                    print("That word was not found in the text.")


            elif decision == "3":
                shift = int(input("Enter shift: "))

                output = formatting(file_string, shift)
                return output


            else:
                raise ValueError

        #The only error that can happen when finding a file is that it is not found.
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        print(f"File {file_name} not found.")
        print(f"These are the list of files{arr}")
        #Recursive call
        shift_cipher()


# def main():
#
#     print(shift_cipher())
# main()
#
