# COMBINATION

# def fact(n):
#     f =1
#     for i in range (1,n+1):
#         f = f*i
#     return f
# m = int(input("Enter number here>>>"))
# l = int(input("Enter number herre>>>"))
# # result = fact(m)/fact(m-l)
# res = fact(m-l) * fact(l)
# result = fact(m)/res
# print(result)

# # SIMPLE INTEREST
# from curses.ascii import SI
# from msilib.schema import Class
# from selectors import SelectSelector


class new():
    def __init__(self):
        self.select = print("1. Simple interest\n2. Principal\n3. Rate\n4. Time")
        # print(self.select)
# new()
class new2(new):
    def __init__(self):
        new.__init__(self)
        self.Select1 = input("Enter any number here>>>")
        if self.Select1 == "1":
            self.p = int(input('Enter principal number>>>'))
            self.r = int(input("Enter the Rate here>>>"))
            self.t = int(input("Enter the time here>>>"))
            self.si = (self.p * self.r * self.t)/100
            print(self.si)
        elif self.Select1 == "2":
            self.s = int(input("Enter simple interest here>>>"))
            self.r = int(input("Enter the rate here>>>"))
            self.t = int(input("Enter the time here>>>"))
            self.P = (self.s * 100)/(self.r * self.t)
            print(self.P)
        elif self.Select1 == "3":
            self.s = int(input("Enter the simple interest here>>>"))
            self.p = int(input('Enter principal number>>>'))
            self.t = int(input("Enter the time here>>>"))
            self.R = (self.s * 100)/(self.p * self.t)
            print(self.R)
new2()


            
  


        