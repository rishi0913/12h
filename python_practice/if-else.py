#1. check input no. is divisible by 2 and 3 
'''i=int(input("enter the no. ; "))
if i%2==0:
    print("no. is divisible by 2")
elif i%3==0:
    print("no. is divisible by 3")
else :
    print("this is a prime no.")'''

#2. check the input year is a leap year or not 
'''n=int(input("enter input"))
if n%4==0:
    print("this is a leap year ")
else:
    print("this is not a leap year")'''

#3. check input three no. which is largest and smallest 
'''n1=int(input("enter no. 1 : "))
n2=int(input("enter no. 2 : "))
n3=int(input("enter no. 3 : "))
if n1>n2 and n1>n3:
    print("no.1 is greatest")
elif n2>n1 and n2>n3:
    print("no.2 is greatest")
elif n3>n1 and n3>n2:
    print("no.3 is greatest")
else:
    print("all no. are equal")'''

#4. check input is a char , digit or special char 
'''ch=input("enter input : ")
if ch.isalpha():
    print("charecter")
elif ch.isdigit():
    print("digit")
else:
    print("special char ")'''

#5. check input character is upper case or lower case
'''ch=input("enter input")
if ch.isupper():
    print("Upper case")
elif ch.islower():
    print("Lower case")
else :
    print("not a char ")'''
