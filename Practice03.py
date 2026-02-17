# Write a program that takes a string use capitalize method also count length of a string
var = "programming for AI"
print(var.capitalize())
print("Length of a string is : ",len(var))

# Q2: How to install module numpy?
# pip install numpy  in terminal

# Q3: Write a program that takes "ABCDEFGH" and prints every 2nd character
var1 = "ABCDEFGHIJK"
print("Every second character : ",var1[1::2])

# Q4: Write a program that stores your name in a variable and prints: "My name is ___ and length is ___"
name = input("Enter your name : ")
print("My name is "+ name + " Length is ",len(name))

# Q5 Write a program that takes "python", removes spaces, and converts to uppercase
text = "       python    "
print(text.strip(" "))

# Q6: Write a program that takes "ABCDEFGHIJK" and prints the string in reverse skipping 2 characters
var2 = "ABCDEGHIJK"
reversed_skipping = var2[::-3]  # Reverse and take every 3rd character
print("Result:", reversed_skipping)

# Q7 Write a program that converts integer 10 into string and concatenates with "apples"
int = 10
var2 = str(int)
print("Apples "+ var2)

# Q8 Write a program that prints the last character of "programming"
var3 = "programming"
print(var3[-1])


# Q9 Write a program that takes "Data Science" and prints characters from index 4 to 8
sub = "Data Science"
print(sub[4:9])

