

from select import select
from ass13b import my

def value():
    print("1. Find simple interest\n2. Find Principal\n3. Find Rate\n4. Find Time")
value()
select = (input("Enter a number here>>>"))

if select == "1":
    p = int(input("Enter the amount here>>>"))
    r = float(input("Enter the rate here>>>"))
    t = float(input("Enter the time here>>>"))
    my.SI(p,r,t)
elif select == "2":
    s = float(input("Enter the simple interest here>>>"))
    r = float(input("Enter the rate here>>>"))
    t = float(input("Enter the time here>>>"))
    my.P(s,r,t)

elif select == "3":
    s = float(input("Enter the simple interest here>>>"))
    p = int(input("Enter the amount here>>>"))
    t = float(input("Enter the time range here>>>"))
    my.R(s,p,t)

elif select == "4":
    s = float(input("Enter the simple interest here>>>"))
    p = int(input("Enter the amount here>>>"))
    r = float(input("Enter the rate here>>>"))
    my.T(s,p,r)

# print('Enter CONTINUE to try again or STOP to terminate operation')
# per = input(">>>").lower()
# if per == 'continue':
#     value()
# else:
#     quit()
   

    