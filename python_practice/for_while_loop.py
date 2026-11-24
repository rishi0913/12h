#1. print no. 1 to n
'''n=int(input("enter input : "))
for i in range(n):
    print(i)'''

#2. print in reverse n to 1 
'''n=int(input("enter input : "))
for i in range (n,1,-1):
    print(i)'''

#3. 3.1 sum of all no .
'''print("enter 5 inputs ")
sum=0
for i in range(5):
    n=int(input("enter input : "))
    sum += n
print(sum)'''

#3.2 product of all no.
'''pr=1
for i in range(5):
    n=int(input("enter input : "))
    pr *= n
print(pr)'''

#3.3 print even no.
'''for i in range(10):
    n=int(input("enter inputs : "))
    if n%2==0:
        print("even no. : ",n)'''

#4. for "perfect no." ex 6,28 matlab 6 divisible by 1,2,3 so 1+2+3=6 
'''n=int(input("enter range input : "))
sum=0
for i in range(1,n):

    if(n%i==0):
        sum+=i
print(sum)
if sum==n:
    print("it is a perfect no. ")
else :
    print("it is not a perfect no.  ")'''

#5.armstrong no ex 153
'''n=int(input("enter no. : "))
original=n
digits=len(str(n))
sum=0

while n>0:
    digit = n%10
    sum += digit**digits
    n= n // 10
print("the no. will be ",sum)
if sum==original:
    print("no. is armstrong")
else :
    print("it is not armstrong")'''
 # 6. 
