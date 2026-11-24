# find area of circle
'''class circle:
    def __init__(self):
        self.radius=int(input("enter input : "))
    def area(self):
            print(3.14*self.radius**2)
x=circle()
x.area()'''

#input three angles and find the triangle is possible or not 
'''class triangle:
    def __init__(self):
        self.i1=int(input("enter value")) 
        self.i2=int(input("enter value")) 
        self.i3=int(input("enter value")) 
    def sum(self):
        tri=self.i1+self.i2+self.i3
        if tri==180:
            print("true triangle")
        else:
            print("not a triangle")

x=triangle()
x.sum()'''

#3. reverse of the no.s 
'''class num:
    def __init__(self):
        self.n=int(input("enter the no. of input you want to take : "))
    def reverse(self):
        for i in range(self.n,0,-1):
            print(i)

x=num()
x.reverse()'''

#4. finding the square of float and integer 
'''class square:
    def __init__(self):
        self.n=int(input("enter the integer input : "))
        self.f=float(input("enter the float input : "))
    def sq(self):
        s1=(self.n)**2
        s2=(self.f)**2
        print("square of integer input : ",s1)
        print("square of float input : ",s2)
x=square()
x.sq()'''

#5. swap two no.s 
'''class num:
    def __init__(self):
        self.n1=int(input("enter input 1st : "))
        self.n2=int(input("enter input 2nd : "))
        print(self.n1,self.n2)
    
    def swap(self):
        self.n1,self.n2=self.n2,self.n1
        print("swaped no.s : ",self.n1,self.n2)

x=num()
x.swap()'''

#6. various methametical operation 
'''class maths:
    def __init__(self):
        self.n1=int(input("enter the input : "))
        self.n2=int(input("enter the input : "))
    def operation(self):
        add = self.n1 + self.n2
        subtract = self.n1 - self.n2
        multiply = self.n1 * self.n2
        divide = self.n1 / self.n2
        print("addition : ",add)
        print("subtraction : ",subtract)
        print("multiplication : ",multiply)
        print("division : ",divide)

x=maths()
x.operation()'''

#7. volume of cube
'''class vol:
    def __init__(self):
        self.s=int(input("enter the length of the side of cube : "))
    def cube(self):
        volume=(self.s)**3
        print("volume of cube will be : ",volume)

x=vol()
x.cube()'''
