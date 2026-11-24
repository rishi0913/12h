#1. take 10 input from user in the list 
'''l=[]
for i in range (11):
    n=int(input("enter input : "))
    l.append(n)
print(l)'''

#2. take 10 user input in the list and calculate he sum 
'''l=[]
sum = 0
for i in range (10):
    n=int(input("enter inputs : "))
    sum += n
    l.append(n)
l1=[sum]
print("list carrying 10 inputs : ",l)
print("list carrying the sum of all inputs in the list : ",l1)'''

#3. reverse the list 
'''l=[]
for i in range (10):
    n=int(input("enter inputs : "))
    l.append(n)
print("normal list : ",l)
l.reverse()
print("reversed list : ", l)'''

#4. even no only in the list 
'''l=[]
for i in range (10):
    n=int(input("enter the input : "))
    if n%2==0:
        l.append(n)
print(l)'''

#5. print odd no.s in the list 
'''l=[]
for i in range (10):
    n=int(input("enter the input : "))
    if n%3==0:
        l.append(n)
print(l)'''

#6. list into the asending order 
'''l=[]
for i in range (10):
    n=int(input("enter random inputs : "))
    l.append(n)
print(l)
l.sort()
print("asending order of list : ",l)'''

#7. sum of odd no. in the list 
'''l=[]
sum=0
for i in range(10):
    n=int(input("enter inputs : "))
    if n%3==0:
        l.append(n)
        sum += n
print(l)
l=[sum]
print("sum : ",l)'''

#8. desending order 
'''l=[]
for  i in range (10):
    n=int(input("enter input : "))
    l.append(n)
print(l)    
l.sort(reverse=True)
print("reversed list : ",l)'''

#9. create 2d list of 3x7 form user input 
'''t1=[]
t2=[]
t3=[]
for i in range (7):
    n=int(input("enter list 1 inputs : "))
    a=int(input("enter list 2 inputs : "))
    b=int(input("enter list 3 inputs : "))
    t1.append(n)
    t2.append(a)
    t3.append(b)
tn=[t1,t2,t3]
print(tn)'''

