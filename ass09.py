class ssd():
    def __init__(self):
        self.pin= "*901#"
        self.access = ('Access Bank\n1>Check Balance\n2>Transfer\n3>Airtime\n4>Other Services\n5>Access Money\n6>Diamond Xtra\n7>XtraCash Loan')
        self.reg()

    def reg(self):
        name = input("Enter your name here: ")
        age = input("Enter your age here: ")
        location = input("Enter your location: ")
        self.confir()
    
    def confir(self):
        self.mypin = input("Enter your pin here>> ")
        if self.mypin == self.pin:
           print (f'{self.access}')
        else:
            print('enter a correct input')

ssd()      

    
    # def access(self):
        
            
# detail = ssd()









# class ssd2():
#     def __init__(self):



   
