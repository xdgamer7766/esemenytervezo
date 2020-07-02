import datetime
class Esemeny:
    def __init__(self,date,name,address,price):
        self.date = date
        self.name = name
        self.address = address
        self.price = price
    def datedifference(self, d1 , d2):
        d1 = datetime.datetime.strptime(self.date, "%Y-%m-%d") 
        d2 = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
        if d1 - d2 > 0:
            return (d1 - d2)
        else:
            return(False)
    def stringconverter(self):
        return ".".join([self.date,self.name,self.address,self.price])

