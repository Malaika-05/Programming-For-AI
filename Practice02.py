# Variables and Datatypes

# Variables
a = 10
b = 10

print(a+b)

# Datatypes
a = 20     #Integer
b = 10
f = 23.8   #Float
g = "Python"  # Strings


# Operators
# 1- Arithmetic operators: +, -, *, / etc.
a = 20
b = 2
print(a+b)  # Addition
print(a-b)  # Subtraction
print(a*b)  #Multiplication
print(a/b)  #Division
print(a%b)  #Modulus

#2. Assignment operators: =, +=, -= etc.
c = 50 #Assignment opearator
c+=10 #Increment
print(c)
d = 20
d-=10 #decrement operator
print(d)


#3. Comparison operators: ==, >, >=, <, != etc.
print(a==20) #Equal Operator
print(a>30)  #Greater than
print(a<=23)  # less than or equal to
print(a!=10)  # is not equal to


#4. Logical operators: and, or, not.
print (" And operator " , True and False)
print (" or operator " , True or False)
print("Not operator ",not True)


# Type operator
print(type(a))
print(type(f))
print(type(g))

# Input function
name = input("What is your name ")
print("Hi ",name)

# Chapter 2 Practice set

# Write a python program to add two numbers

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
print("The Sum of two numbers is : ",num1+num2)

# Write a python program to find remainder when a number is divided by z
num3 = int(input("Enter the Dividened : "))
num4 = int(input("Enter the divisor : "))
print("The remainder of the two numbers : ",num3%num4)

# Check the type of variable assigned using input () function.
var = input("Enter anything to find its type : ")
print(type(var))


# Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80
var1 = 34 
var2 = 80
print("The num1 is greater than num2 : ",var1>var2)

# Write a python program to find an average of two numbers entered by the user
var3 = int(input("Enter num1 : "))
var4 = int(input("Enter num2 : "))
print("The Average of two numbers is : ",(var3+var4)/2)

# Write a python program to calculate the square of a number entered by the user.
var5 = int(input("Enter the number : "))
print("The square of number is : ",var5*var5)
