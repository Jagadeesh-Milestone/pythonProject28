#class/instance/static methods in a single class
class milestone:
    myname='jagadeesh'
    def friends(self):
        friendname='hari'
        print(self.myname,friendname,'are friends')
    @staticmethod
    def friend():
        friendname='mahesh'
        print(friendname,milestone.myname,'are friends')
    @classmethod
    def frnds(cls):
        friendname='rupesh'
        print(cls.myname,friendname,'are friends')
obj1=milestone()
obj1.friends()

obj2=milestone()
obj2.friend()

obj3=milestone()
obj3.frnds()