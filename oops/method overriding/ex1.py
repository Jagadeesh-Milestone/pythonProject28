#method overriding:
class parent:
    def mobile(self):
        print('ill give 15000 to buy a mobile')
class child(parent):
    def mobile(self):
        print('ill buy a mobile for 20000')
c=child()
c.mobile()