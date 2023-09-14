#arbitary arguments *args
#when you dont know how many values you are passing then put a
#* before the argument name

def d1(*students):
    print(students)
    print(students[0])
    print('the tallest student is',students[2])
d1('hari','jagadeesh','suresh','naresh','manoj')