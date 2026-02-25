# Lists and tuples

# Lists
l1 = [7,8,1,5,9,3,6,4]
print(type(l1)) # lists

# Methods for the lists
l1.insert(4,10)  # at index 4 the number 10 will be added
l1.sort() # sort the list in ascending order
l1.reverse() # it will reverse the list  [4, 6, 3, 9, 5, 1, 8, 7]
l1.sort(reverse=True) #[9, 8, 7, 6, 5, 4, 3, 1] sort the  descending order
l1.append(2) #[9, 8, 7, 6, 5, 4, 3, 1, 2] will add the 2 at the end of list
l1.pop(7)   #[9, 8, 7, 6, 5, 4, 3, 2] at index 7 the number 1 is removed
l1.remove(9)   #[8, 7, 6, 5, 4, 3, 1] 9 is remove
print(l1)


# Tuples  A tuple is an immutable data type in python.
t1 = (7,9,4,5,6,3,2,1)
print(type(t1))
print(t1.count(9))  # how many 9 is occur in the tuple #1
print(t1.index(2))  # the number 2 is on the index 6 so the output is 6

# Practice set
# Write a program to store seven fruits in a list entered by the user

fruits = []
f1 = input("Enter fruit ")
fruits.append(f1)
f2 = input("Enter fruit ")
fruits.append(f2)
f3 = input("Enter fruit ")
fruits.append(f3)
f4 = input("Enter fruit ")
fruits.append(f4)
f5 = input("Enter fruit ")
fruits.append(f5)
f6 = input("Enter fruit ")
fruits.append(f6)
f7 = input("Enter fruit ")
fruits.append(f7)

print(fruits)

# Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
s1= input('Enter marks : ')
marks.append(s1)
s2 = input('Enter marks : ')
marks.append(s2)
s3= input('Enter marks : ')
marks.append(s3)
s4= input('Enter marks : ')
marks.append(s4)
s5= input('Enter marks : ')
marks.append(s5)
s6= input('Enter marks : ')
marks.append(s6)
print(marks)

#Q3 Check that a tuple type cannot be changed in python.

t2 = (3,8,9,4)
t2[4] = 6 # will give error because we cannot add to the tuple
print(t2) 

# Q4 Write a program to sum a list with 4 numbers.
l2 = [1,2,3,4]
print(sum(l2))

# Q5 Write a program to count the number of zeros in the following tuple:
t3 = (7, 0, 8, 0, 0, 9)
print(t3.count(0))