#static attribute:
#to declare a variable statically we use @staticmethod
class milestone:
    @staticmethod
    def d1():
        x="I am a static attribute"
        print(x)
x=milestone()
x.d1()#using instance creation

milestone.d1()#using class name