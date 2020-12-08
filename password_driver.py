


from Password import Password


def main():

    my_pass = Password("hello.")

    length = my_pass.get_length()
    print(length)

    length_score = 0
    if 5 <= my_pass.get_length() < 8:
        length_score = 1
    elif my_pass.get_length() < 4:
        length_score = - 10
    elif 8 <= my_pass.get_length() <= 10:
        length_score = 3
    elif my_pass.get_length() > 10:
        length_score = 7

    character_score = 0
    if my_pass.contain_capital():
        character_score += 1

    if my_pass.contain_lower_case():
        character_score +=1

    if my_pass.contain_symbol():
        print("contains symbol")

main()