def d1(text):
    return text.upper()

def d2(text):
    return text.lower()

def d3(a):
    result=a('Hello World')
    print(result)
d3(d1)
d3(d2)