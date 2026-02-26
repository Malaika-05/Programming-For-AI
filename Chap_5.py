# s = {
#     "Name" : "Malaika Taqveem ",
#     "Roll no ": 83,
#     "Subjects ": ["AI","Database","statistics","Python"]
# }
# print(s.keys()) #dict_keys(['Name', 'Roll no ', 'Subjects '])
# print(s.values()) #dict_values(['Malaika Taqveem ', 83, ['AI', 'Database', 'statistics', 'Python']])
# print(s.items()) #dict_items([('Name', 'Malaika Taqveem '), ('Roll no ', 83), ('Subjects ', ['AI', 'Database', 'statistics', 'Python'])])
# print(s.get("Name")) #Malaika Taqveem


# Sets
# a = set()
# print(type(a))
# a.add(3)
# a.add(3)
# a.add(7)
# a.add(5)
# a.add(8)
# print(a) #{8, 3, 5, 7}

# b = {8, 3, 5, 7}
# print(len(b)) # 4
# b.remove(5) #{8, 3, 7}
# b.pop() #{3, 7} remove random value in the set
# b.clear() #set()
# print(b)
# c = {1,2,3,4,5,6}
# d = {6,7,8,9}
# print(c.union(d)) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(c.intersection(d)) #{6}


# Chapter 5 practice set

#Write a program to create a dictionary of urdu words with values as their English translation. Provide user with an option to look it up!

# words = {
#     "house": "Ghar",
#     "street": "Gali",
#     "tea": "Chai",
#     "water": "Paani",
#     "cat": "Billi",
#     "parrot": "Mithu"
# }

# choice = input("Enter your choice: ").lower()
# print(words[choice])

# Write a program to input eight numbers from the user and display all the unique numbers (once).= 
# numbers = set()
# print(type(numbers))
# num1 = int(input("Enter the number : "))
# numbers.add(num1)
# num2 = int(input("Enter the number : "))
# numbers.add(num2)
# num3 = int(input("Enter the number : "))
# numbers.add(num3)
# num4 = int(input("Enter the number : "))
# numbers.add(num4)
# num5 = int(input("Enter the number : "))
# numbers.add(num5)
# num6 = int(input("Enter the number : "))
# numbers.add(num6)
# num7 = int(input("Enter the number : "))
# numbers.add(num7)
# num8 = int(input("Enter the number : "))
# numbers.add(num8)
# print(numbers)

# Can we have a set with 18 (int) and '18' (str) as a value in it?
z = set()
z.add(18)
z.add("18")
print(z)

# What will be the length of following set s:
y = set()
y.add(20)
y.add(20.0)
y.add('20') # length of s after these operations?
print(y) #{20, '20'}

# What is the type of 's'?
x = {}
print(type(x)) #<class 'dict'>

# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique
dic = {}
name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
dic.update({name:lang})
name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
dic.update({name:lang})
name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
dic.update({name:lang})
name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
dic.update({name:lang})
print(dic)


# If the names of 2 friends are same; what will happen to the program in problem 6?
# Enter your name : Malaika
# Enter your favourite language : Pushto
# Enter your name : Sara
# Enter your favourite language : Pushto
# Enter your name : Zara
# Enter your favourite language : Urdu
# Enter your name : ALexa
# Enter your favourite language : English
# {'Malaika': 'Pushto', 'Sara': 'Pushto', 'Zara': 'Urdu', 'ALexa': 'English'}

# If languages of two friends are same; what will happen to the program in problem 6?
# Enter your name : Malaika
# Enter your favourite language : Pushto
# Enter your name : Malaika
# Enter your favourite language : English
# Enter your name : Sara
# Enter your favourite language : Urdu
# Enter your name : Zara
# Enter your favourite language : French
# {'Malaika': 'English', 'Sara': 'Urdu', 'Zara': 'French'}

#  Can you change the values inside a list which is contained in set S?
g = {8, 7, 12, "Harry", [1,2]}
# No, you cannot change the values inside a list contained in a set because lists are mutable and cannot be elements of a set. 
# Therefore, such a set cannot be created in Python.


