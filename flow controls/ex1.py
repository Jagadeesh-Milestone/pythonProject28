#flow controls or conditional statements
#if
#else
#elif
#nested if
# if:
#if returns true if the given statement is true
a=10
b=20
if a<b:
    print('condition is true/if block executed')
else:
    print('condition is false/else block executed')

#and
user='jagadeesh'
password=8989
if user=='jagadeesh' and password==8989:
    print('access granted')
else:
    print('access denied')

#or
if user=='jagadesh' or password==8988:
    print('access granted')
else:
    print('access denied')

#user input:
#username=input('enter your username:')
#pin=int(input('enter your pin:'))
#if username=='jagadeesh' and pin==7878:
#   print('login successful')
#else:
#    print('login failed')

username=input('enter your username:')
pin=int(input('enter your pin:'))
if username=='jagadeesh' or pin==7878:
    print('login successful')
else:
    print('login failed')

