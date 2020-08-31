
# num1= int(input( "Enter first number :"))
# num2= int(input(" Enter second number :"))
# sum_of_var= num1+num2
# print(sum_of_var-10)

# num1= float(input( "Enter first number :"))
# num2= float(input(" Enter second number :"))
# sum_of_var= num1+num2
# results= sum_of_var-10
# print(" Sum is {}".format(results))

# num1= float(input( "Enter first number :"))
# num2= float(input(" Enter second number :"))
# results= num1+num2
# print(" Sum is {}".format(results))


# a= float(input("Enter the value : "))
# b= float(input("Enter the second value: "))
# results= (a+b)
# print("The sum of your value is : {}".format(results))
# print("Double of the  results of a and b : {}". format(results*2))

"""
Consider you have a post paid mobile with a monthly bill of 500 which will give you 50 calls
 and 20 messages for free. If the calls and messages are increased the bills get increased
 0.57 per call and o.25 per message. Take the input from the user for the calls and messages made
 and calculate the total bill.
"""

#
# base_price=500
# total_calls= float(input("Enter the number of calls: "))
# total_messages= float(input("Enter the number of message: "))
# if total_calls >50:
#     extra_call=total_calls-50
#     extracall_price=extra_call*0.75
# else:
#     extracall_price=0
# if total_messages>20:
#     extra_message=total_messages-20
#     extramessage_price=extra_message*0.25
# else:
#     extramessage_price=0
#
# extra_price=extracall_price+extramessage_price
# print(" Total bill is {} ".format(500+extra_price))



# Elif


"""
Write a programme which will take numbers from 0- 2000 and print 
all the numbers which are divisible by 10. 
"""


# for i in range (0,101):
#     if i%7 ==0:
#         print(i)


# foor loops
# name="Diraj Sharma"
# result=" "
# for letter in name:
#     result=result+letter
#     print(result)

#
# for diraj in range(0,10): # this takes the number up to 9.
#     print(diraj)

# nested for loopa

# for diraj in range(0,10): # this takes the number up to 9.
#     for sharma in range(2,4):
#     print(diraj)

# Write a programme to print numbers from 0-10 except for 3 and 6 and stop printing after printing 9.

# for i in range (0,12):
#     if i ==3 or i==6:
#         continue
#     if i==10:
#         break
#     else:
#         print(i)
#
#


# for i in range (0,12):
#     if i ==3 or i==6:
#         continue
#     if i==9:
#         print(i)
#         break
#     else:
#         print(i)
#


# Write a programme to print numbers from 0-10 except for 3 and 6 and stop printing after printing 9.
# i=0
# while i<12:
#     if i ==3 or i==6:
#         i=i+1
#         continue
#     if i==9:
#         print(i)
#         break
#     else:
#         print(i)
#         i = i + 1
#
#



# Write a programme to print numbers from 0-10 except for 3 and 6 and stop printing after printing 9.


# for i in range (0,12):
#     if i ==3 or i==6:
#         continue
#     if i==10:
#         break
#     else:
#         print(i)

# Write a programme to print numbers from 0-10 except
# for 3 and 6 and stop printing after printing 9.
#
# for i in range(0,12):
#     if i==3 or i==6:
#         continue
#     if i==10:
#         break
#     else: print(i)
#

#
# for i in range(0,12):
#     if i==3:
#         continue
#     if i==6:
#         continue
#     if i==10:
#         break
#     else:
#         print(i)
#


#
# i=0
# while i<12:
#     if i ==3 or i==6:
#         i=i+1
#         continue
#     if i==9:
#         print(i)
#         break
#     else:
#         print(i)
#         i+=1



# for i in range (0,12):
#     if i==3 or i==6:
#         continue
#     if i==9:
#         break
#     else:
#         print(i)


#
# for diraj in range(0,10):
#     for sharma in range(2,4):
#         print ("the results= {}*{}={}".format(diraj,sharma,diraj*sharma) )


# for diraj in range (2,9):
#     for sharma in range(1,10):
#         print(" {}* {} = {}". format(diraj,sharma,diraj*sharma)) # ? format



# guessing game
#
# secret_word="diraj"
# guess=""
# guess_cont=0
# guess_limit=5
# out_of_guess= False
# while guess!=secret_word and not out_of_guess:
#     if guess_cont <5:
#         guess_cont = 1 + guess_cont
#         guess= input("Enter guess:")
#     else:
#         out_of_guess= True
# if out_of_guess:
#     print( "Looser")
# else:
#     print("Winner")



# Guess secret number

# secret_number=40
# guess=""
# guess_limit=5
# guess_count=0
# out_of_guess=False
# while guess!=secret_number and not out_of_guess:
#     if guess_count<guess_limit:
#         guess_count=1+guess_count
#         guess= input("Enter Guess Number : ")
#         out_of_guess=True
#         if guess <60:
#             print("The number is too high")
#     else: not completed

# n=18
# number_of_guesses=1
# print("Number of guesses are limited to 5 times.")
# while number_of_guesses<=5:
#     guess_number= int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("You enter less number please input greater number. \n")
#     elif guess_number>18:
#         print("You entered greater number please input smaller number. \n")
#     else:
#         print("You won\n")
#         print(number_of_guesses, "No of guesses you took to finish.")
#         break
#     print(5-number_of_guesses, "No of guesses left")
#     number_of_guesses= number_of_guesses+1
# if number_of_guesses>5 :
#     print("Game Over : You loose")



# n=10
# number_of_guesses=1
# print("Number of guesses are limited to 5 times.")
# while number_of_guesses<=5:
#     guess_number= int(input("Guess the number :\n"))
#     if guess_number<10:
#         print("You enter less number please input greater number. \n")
#     elif guess_number>10:
#         print("You entered greater number please input smaller number. \n")
#     else:
#         print("You won\n")
#         print(number_of_guesses, "No of guesses you took to finish.")
#         break
#     print(5-number_of_guesses, "No of guesses left")
#     number_of_guesses= number_of_guesses+1
# if number_of_guesses>5 :
#     print("Game Over : You loose")

#
#
# Secret_num=10
# guess_count=1
# while guess_count<=5:
#     guess_num=



# Take numbers from 0-100 and print the numbers divisiable by 5

# for i in range(0,100):
#     if i%5==0:
#         print(i)
#

# [12,34,56,78,90,9,87,65,43,22,3,4,5,6,7,8,76,51
#     ,23,45,67,9,87,65,34,56,78,76,53,456,788,765,432,345,678,998,765,4,32,34,567,890]
#
# # From the above list print all the numbers which are divisible by 3 and greather then 55.
# my_list=[12,34,56,78,90,9,87,65,43,22,3,4,5,6,7,8,76,51
#     ,23,45,67,9,87,65,34,56,78,76,53,456,788,765,432,345,678,998,765,4,32,34,567,890]
# for item in my_list:
#     if item>55:
#         if item %3==0:
#             if item %2==0:
#                 if item%5==0:
#                     results=item/8
#                     print(results)
#
# exercise 1 print(" Diraj Sharma \n 1401 Liberty Street \n El Cerrito CA 948054\n USA")
# exercise 2
# lenght= float(input("Enter the lenght of your room : "))
# width= float(input("Enter width of your room : "))
# size_of_room= str(lenght*width)
# print(str(size_of_room +" Feet"))


# exercise 2
# lenght= float(input("Enter the lenght of your room : "))
# width= float(input("Enter width of your room : "))
# size_of_room= (lenght*width)
# print("Size of room is {} Squire Feet".format(lenght*width ))

# exercise 3
# lenght_of_field = float(input("Enter the lenght of your field in feet : "))
# width_of_field=  float(input("Enter width of your field in feet: "))
# size_of_field= (lenght_of_field*width_of_field)
# print("Size of field is {} Acres".format(size_of_field/43560))

"""
1>=0.10 
1<0.25 

"""
# num_small_container= float(input("Number of containers Equal or less than 1 liter "))
# num_big_container= float(input("Number of containers bigger than 1 liter "))
# deposit_for_smaller_container=num_small_container*0.10
# deposit_for_big_container=num_big_container*0.25
# total_price= deposit_for_smaller_container*deposit_for_big_container
# print(" Total refund is $ {} ".format(deposit_for_smaller_container*deposit_for_big_container "))


# cost_of_meal= float(input(" Cost of the meal "))
# tips=(18/100)*cost_of_meal
# tax=(15/100)*cost_of_meal
# total_amount=print("Total amount after tax is $ {}".format(cost_of_meal+tips+tax))



# a=float(input(" Enter first number "))
# operation=(input("Enter operator sign")
# b=float(input("secd number"))
# results=
# cost_of_meal= float(input(" Cost of the meal "))
# tips=(18/100)*cost_of_meal
# tax=(15/100)*cost_of_meal
# total=cost_of_meal+tips+tax
# print("Total amount is $ {}".format(round(total,2)))

# total_amount=print("Total amount after tax is $ {}".format(round(cost_of_meal+tips+tax)))

# sum = n(n+1)/2

# number=int(input(" Enter number: "))
# sum_of_number=(number*(number+1))/2
# print(sum_of_number)
# n= int(input("enter a number: "))
# my_list=[]
# for i in range(0,n):
#     my_list.append(i+1)
# print(my_list )
# print(sum(my_list))

# n= int(input("enter a number: "))
# my_list=[]
# for i in range(0,n+1):
#     my_list.append(i)
# # print(my_list )
# print(sum(my_list))













# a=int(input("Enter first num : "))
# operator= input("Enter operator")
# b=int(input("Enter second num: "))
# if operator== "+":
#     print(a+b)
# elif operator== "-":
#     print(a-b)
# elif operator== "/":
#     print(a/b)
# elif operator== "*":
#     print(a*b)
# else:
#     print("Invald operator")
#
# #
# a=int(input("Enter first num : "))
# operator= input("Enter operator: ")
# b=int(input("Enter second num: "))
# if operator== "+":
#     print(a+b)
# elif operator== "-":
#     print(a-b)
# elif operator== "/":
#     print(a/b)
# elif operator== "*":
#     print(a*b)
# elif operator== "%":
#     print(a%b)
# elif operator =="**":
#     print(a**b)
# else:
#     print("Invald operator")


# write a program to take input from the user until
# the number is 0 and find the sum of all the items in the list


# num=[]
# n= float(input("Enter a number: "))
# while n!=0:
#     num.append(n)
#     n=float(input("Enter another number: "))
# # print(sum(num))
# print("The sum of the number you entered is: {:.2f}".format(sum(num)))


num=[]
# n= float(input("Enter a number: "))
# while n!=0:
#     num.append(n)
#     n=float(input("Enter another number: "))
# # print(sum(num))
# print("The sum of the number you entered is: {:.2f}".format(sum(num)))




# create functions one will be toal anod another will be agerage.  a function called student which will take the marks of four subject
# as input and calculate the total of it's avrage
# 
# def total()
# def average()

#OPPS- Object oriented programs
# Class- Blueprint -Methods( Functions)
# Object- Properies(Varibales), methods- Instance of class
# Special Fuctions =__function__()
# types-4
# 1. Abstraction- Showing only what is neccessay
# 2. Inheritaance- Grandfather- Father- Son
# 3. Encapsulation- Binding the properties and metthds with one entity
# 4. Polymorphism- One person doing multiple task or things

#
# class mobile:
#     def __init__(self):
#         self.name=input("Enter the model name: ")
#         self.storage=int(input("Enter the size: "))
#     def details(self):
#         print("iphone {}, {} gb".format(self.name,self.storage))
#
# iphone6=mobile()
# iphone6.details()
# iphone10=mobile()
# iphone10.details()
#

# class mobile:
#     def __init__(self):
#         self.name=input("Enter the model name: ")
#         self.storage=int(input("Enter the size: "))
#     def details(self):
#         print("iphone {}, {} gb".format(self.name,self.storage))
#
# d=mobile()
# d.details()
# s=mobile()
# s.details()
#


#
#
# class A:
#     def __init__(self):
#         print("init A")
#
#     def function1(self):
#         print("function1")
#
# class B:
#     def __init__(self):
#         print("init B")
#
#     def function2(self):
#         print("function2")
#
# class C:
#     def __init__(self):
#         print("init C")
#
#     def function3(self):
#         print("function2")
#
#
#
# diraj=A()
# Mounish=B()
# Maanoj=C()
#
"""
1. Write a program that reads an integer from the user. 
Then your program should display a message
 indicating whether the integer is even or odd.

"""
# num=int(input("Enter a number:" ))
# if num%2==0:
#     print(" The number you typed is even.")
# else:
#     print("It is odd number")



"""
2. In this exercise you will create a program that reads a 
letter of the alphabet from the user.
 If the user enters a, e, i, o or u then your program should display a message indicating 
 that the entered letter is a vowel. If the user enters y then your program should display a 
 message indicating that sometimes y is a vowel, and sometimes y is a consonant. 
 Otherwise your program should display a message indicating that the letter is a consonant.
 
"""
# vowel=["a", "e", "i","o","u"]
# for item in vowel:
#     if

# letter= (input(" Enter a letter: "))
# if letter == "a":
#     print(" You you typed a vowel.")
# if letter == "e":
#     print(" You you typed a vowel.")
# if letter == "i":
#     print(" You you typed a vowel.")
# if letter == "o":
#     print(" You you typed a vowel.")
# if letter == "u":
#     print(" You you typed a vowel.")
# elif letter== "y":
#     print("letter 'Y' is sometime vowel and some time consonant.")
# else:
#     print("You entered a consonant.")


#
# letter= str(input(" Enter a letter: "))
# if letter == "a"/"e":
#     print(" You you typed a vowel.")
# elif letter== "y":
#     print("letter 'Y' is sometime vowel and some time consonant.")
# else:
#     print("You entered a consonant
import pandas









letter = input("")
if letter in "AEIOUaeiou":
    print("The letter is vowel")
elif letter in "Yy":
    print("Sometime vowel sometime consonant")

else:
    print("Consonant")


