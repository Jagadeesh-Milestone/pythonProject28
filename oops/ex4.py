#instance attribute:
#the variable which is taken inside the function of a class is
#called instance attribute:
class milestone:
    def d1(self):
        x="i am a instance attribute"
        print(x)
obj1=milestone()
obj1.d1() #objectname.function name

obj2=milestone()
obj2.d1()

#if we have a method as object.method(self,arg1,arg2) we have to pass
#values for arg1,arg2 only and the value for self will be automatically
#provided by python.
