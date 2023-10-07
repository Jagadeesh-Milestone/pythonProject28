#atm use case:
while True:
    balance=50000
    print('    welcome to ICICI bank     ')
    print('1.balance\n 2.withdraw\n 3.deposit\n 4.quit')
    option=int(input('enter your option:'))
    if option==1:
        print('your account balance is:',balance)
        break
    if option==2:
        print('balance is :',balance)
        withdraw=int(input('enter the amount to withdraw:'))
        if withdraw>0 and withdraw<balance:
            remainingbalance=balance-withdraw
            print('withdraw of',withdraw,'rupees done successfully')
            print('remaining balance is:',remainingbalance)
            break
        else:
            print('no withdraw done')
            break
    if option==3:
        print('balance is :',balance)
        deposit=int(input('enter the amount to deposit:'))
        if deposit>0:
            updatedbalance=balance+deposit
            print('deposit of',deposit,'rupees done successfully')
            print('updated balance is:',updatedbalance)
            break
        else:
            print('no deposit done')
            break
    if option==4:
        exit()
        break
    else:
        print('enter only 1,2,3 or 4')
        break








