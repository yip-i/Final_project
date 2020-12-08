"""
Shift cipher decoder
If you know one word in the word,
you can decrypt the whole message.

"""
#actual_string

encrypted_string = "HS RSX KS KIRXPI MRXS XLEX KSSH RMKLX BCD"

"""
Find Shift.
Function
Find the shift of the words 
parameters: list of strings and known word

"""
def find_shift(list_strings, known_word):

    for i in list_strings:

        shift = ord(i[0]) - ord(known_word[0])

        if chr(ord(i[1]) - shift) == (known_word[1]):
            return(shift)





"""
Find length of target word
parameters: strings, word that you know is in the sentence
return list of strings that are the same length as the word

"""


def same_length(sentence, known_length):
    same_length_words = []
    for i in sentence.split():
        if len(i) == known_length:
            same_length_words.append(i)

    return(same_length_words)

"""
Translates the shifted cipher into regular text.
Parameters: The coded string of words and the shift of each character.
Return should be the string.

"""

def translate(coded_string, shift):
    coded_list = coded_string.split()
    decrypted_list = []
    string = ""

    for i in coded_list:
        for x in range(len(i)):
            if (ord(i[x]) - shift) >= 65 and (ord(i[x]) - shift) <=90:
                string += chr(ord(i[x]) - shift)
            else:
                string += chr(ord(i[x]) - shift + 26)
        string += " "

    print(string)




def main():

    word_you_know = "Night"
    word_you_know = word_you_know.upper()
    length_you_know = len(word_you_know)

    #Find words that are the same length as the one that you know
    list_same_length = same_length(encrypted_string, length_you_know)

    # Find how much each character has shifted by
    shift = find_shift(list_same_length , word_you_know)

    translate(encrypted_string,shift)









main()

