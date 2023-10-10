class rbi:
    def rateofintrest(self):
        return 0
class sbi(rbi):
    def rateofintrest(self):
        return 2
class hdfc(rbi):
    def rateofintrest(self):
        return 3
class icici(rbi):
    def rateofintrest(self):
        return 3.5
i=icici()
print(i.rateofintrest())

h=hdfc()
print(h.rateofintrest())