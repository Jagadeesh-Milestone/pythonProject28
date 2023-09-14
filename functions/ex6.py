#**kwargs
#we can pass keyword arguments by using **before argument name

def d1(**employee):
    print(employee)
    print(employee['emp2'])
    print('hard working employee is',employee['emp1'])
d1(emp1='hari',emp2='manoj',emp3='naresh')