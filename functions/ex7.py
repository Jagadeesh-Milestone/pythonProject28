#default arguments
def d1(country='India'):
    print("I am From",country)
d1('australia')
d1()
d1()
d1('england')
d1()

def d2(a,b=100):
    print(a+b)
d2(10,20)
d2(200)
d2(500)
d2(300,400)