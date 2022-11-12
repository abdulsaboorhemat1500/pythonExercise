import sys

# working with try,except,esle and finally block

# num1 = input("please Enter any value")
# num2 = input("please Enter any value")

# try:
#    result = int(num1)/int(num2)

# except ZeroDivisionError:
#    print(sys.exc_info()[0])
#    print("oops! can't divided by zero please enter another value ")
# else:
#    print("success!!!!")

# finally:
#    print("this is finally block !")

# another example in raising exception 

number = int(input("enter any positive integer value  : "))

if number <0:
   raise ValueError("oops! this is not a positive value ")
else:
   print("you entered a positive value " , number)





# raising exception  

# num = input("enter any value :  ")

# if not type(num) is int:
#    raise Exception("only integer type accepted ! ")

# print("success !!! ")



#  checking email via raising exception 

# email = input("enter your email address : ")

# if not "@gmail.com" in email:
#    raise Exception("invalid email address ! ")

# print("your email is valid  " + email)