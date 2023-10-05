#class method
class milestone:
    myname='jagadeesh'
    friendname='hari'
    @classmethod
    def friends(cls):
        print(cls.myname,'and',cls.friendname,'are best friends')
milestone.friends()

obj=milestone()
obj.friends()