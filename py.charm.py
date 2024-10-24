#Minaya A

def encode(digits):
    print("Your password has been encoded and stored!\n")
    new_password = ''
    for i in range(len(password)):
        new_password  += str((int(password[i]) + 3) % 10)
    return new_password

if __name__ == '__main__':
    choice = 0
    while choice != '3':
        print('Menu')
        print('-------------')
        print('1.Encode')
        print('2.Decode')
        print('3.Quit')
        print()
        choice = input("Please enter an option: ")
        if choice == '1':
            password = input("Please enter your password to encode: ")
            new_password = encode(password)
        elif choice == '2':
            pass
        elif choice == '3':
            break