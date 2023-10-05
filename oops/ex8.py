#methods:
#methods are the functions inside a class.
#there are three types of methods in python oops
#class method
#instance method
#static method

#instance method:
class milestone:
    productid=909098
    def product(self):
        self.productname='oneplus'
        self.productcost=25000
        print('product name:',self.productname,'product cost:',self.productcost)
        print(self.productid)
obj=milestone()
obj.product()