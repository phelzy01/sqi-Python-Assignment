# # EMAIL
import re
def email():
    m = input('Enter your email: ')
    # p = input('Enter your password: ')
    mm = re.search(r"[@gmail.com,@email.com,@yahoo.com]$",m)
    if mm:
        print('we have a match')
    else :
        print('Invalid input')
        email()
email()


    
