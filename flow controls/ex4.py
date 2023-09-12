#nested if
a=50
if a<60:
    print('a is less than 60')
    if a>70:
        print('a is also less than 70')
    else:
        print('a is not greater than 70')
        if a==50:
            print('a is equals to 50')
            if a!=50:
                print('a is not equals to 50')
            else:
                print('a is equal to 50')
                if a>40:
                    print('a is greater than 40')