#1. take 10 input form user 
# for creating the se we use open bracates "()"
'''s=set ()
for i in range (10):
    n=int(input("enter inputs : "))
    s.add(n)
print(s)'''

#2. convert list into set
'''l=[1,2,3,4,5,6]
print(l)
s=set(l)
print(s)'''

#3.merge two sets 
'''s1={1,2,3}
s2={"a","b","c"}
s1.update(s2)
print(s1)'''

#4. sum of all no. in the list
'''s=set()
sum=0
for i in range (5):
    n=int(input("enter inputs"))
    s.add(n)
    sum+=n

print(s)
print("sum of no present in the list : ",sum)'''

#5. product of all inputs
'''s=set()
pr=1
for i in range(3):
    n=int(input("enter input : "))
    s.add(n)
    pr*=n

print(s)
print("product : ",pr)'''

#6. creating a set of even no. present on set 2 
s1=set()
s2=set()
for i in range(10):
    n=int(input("enter inputs"))
    s2.add(n)
    if n%2==0:
        s1.add(n)
print(s2)
print("even no. : ",s1)
