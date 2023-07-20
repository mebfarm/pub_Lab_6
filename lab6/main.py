# Michael Bailey


# This is a sample Python script.


def menu():
    print('\nMenu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def encode(passwd):
    s_to_int = [(int(i) + 3) % 10 for i in passwd]

    out = [str(i) for i in s_to_int]
    out_1 = "".join(out)
    return out_1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    code_on = True
    encoded_password = ''
    while code_on:
        menu()
        option = int(input('\nPlease enter an option: '))
        if option == 1:
            pass_word = input('Please enter your password to encode: ')
            encoded_password = encode(pass_word)
            print(type(encoded_password))
            print('Your password has been coded and stored!')
        elif option == 2:
            original = decoder(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original passcode is {original}. ')
        elif option == 3:
            code_on = False





