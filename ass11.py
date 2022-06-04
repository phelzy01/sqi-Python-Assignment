from math import factorial
from ass11b import my
print("1. Add\n2. Sub\n3. Mul\n4. Div\n5. Fac\n6. Per")
inp = input("Enter number here>>> ")

if inp=="1":
    va = int(input("Enter any number here>>>"))
    va2 = int(input("Enter any number here>>>"))
    my.add(va,va2)

elif inp =="2":
    va = int(input("Enter any number here>>>"))
    va2 = int(input("Enter any number here>>>"))
    print(my.sub(va,va2))

elif inp =="3":
    va = int(input("Enter any number here>>>"))
    va2 = int(input("Enter any number here>>>")) 
    (my.mul(va,va2))


elif inp == "4":
    va = int(input("Enter any number here>>>"))
    va2 = int(input("Enter any number here>>>"))
    (my.div(va,va2))

elif inp == "5":
    va = int(input("Enter the number here>>>"))
    print(my.fact(va))

elif inp == "6":
    va = int(input("Enter number here>>>"))
    va2 = int(input("Enter number here>>>"))
    

