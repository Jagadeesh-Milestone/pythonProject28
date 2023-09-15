#nested function
#a function taking inside another function
#the main function is called outer function and the function
#which is inside the outer function is called inner function

def d1():
    print('hello world')
    def d2():
        print('hello python')
    d2()
d1()
