print('welcome to python bank ATM')
restart=('Y')
chances = 3
balance = 999.12
while chances >= 0:
    pin = int(input('please Enter your 4 digit pin: '))
    if pin == (1234):
        print('you entered your pin correctly')
        print('please press 1 for your balance')
        print('please press 2 to make a withdraw')
        print('please press 3 to pay in')
        print('please press 4 to return card')
        option = int(input('what would you like to choose?: '))
        if option == 1:
            print('your balance is $', balance)
            restart = input('would you like to go back?: ')
            if restart in ('n', 'NO', 'no', 'N'):
                print('Thank you')
                break
        elif option == 2:
            option2 = ('y')
            withdrawl = float(input('How much would you like to withdraw? 10,20,40,60,80,100 for other enter 1: '))
if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print('\nYour Balance is now $',balance)
                    restart = input('would you like to go back')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank you')
                        break
                 elif withdrawl != [10, 20, 40 ,60 ,80, 100]:
                    print('Invalid Amount, please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('please Enter Desired amount:'))

            elif option == 3:
                Pay_in = floar(input('How muc would you like to pay in? '))
                balance = balance + Pay_in
                print('\nYour balance is now $',balance)
                restart = input('would you like tp go back')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank you')
                    break

            elif option == 4:
                print('please wait whilst your card is Returned....\n')
                print('Thank you for your service')
                break
            else:
                print('please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break