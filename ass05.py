# MULTIPLICATION
# num = int(input('Enter the number>'))
# for i in range(1,13):
#     print(num, 'x', i,'=', num*i)

# for i in range(1,11):
#     for n in range(1,13):
#         print(i,'x',n,'=',i*n)

# EVEN AND ODD NUMBER
# even = []
# odd = []
# prime = []
# for i in range(1,11):
#     que = int(input('Enter number: '))
#     if que%2 == 0:
#         even.append(que)
#     else:
#         odd.append(que)
# print(even)
# print(odd)


# PRIME NUMBERS
# lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
# upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
# print ("The Prime Numbers in the range are: ")  
# for number in range (lower_value, upper_value + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number) 

# Another method for prime number
for i in range(2,11):
    for n in range(2,i):
        if i%n == 0:
            print(i,'is not a prime number')
            break
        else:
            print(i,'is a prime number')


