name = "Harry"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3) # har
print(nameshort)  
character1 = name[1] # a
print(character1)


print(name[0:3]) #Har

print(name[-4: -1]) #arr
print(name[1:4])   #arr

print(name[:4]) # is same as print(name[0:4]) #Harr
print(name[1:]) # is same as print(name[1:5]) #arry
print(name[1:5]) # arry



print(len(name)) #5
print(name.endswith("rry")) #True
print(name.startswith("ha")) #False
print(name.capitalize()) #Harry

a = 'Harry is a good boy\nbut not a bad \'boy\'' # Escape Sequence
print(a)


# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
user = input("Enter our name : ")
print(user + " Good Afternoon")
# print(f"Good Afternoon, {name} ") 

#  Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|> 
'''
template = letter.replace("<|Name|>"," Malaika").replace("<|Date|>", " 24/02/2026")
print(template)


# 3-Write a program to detect double space in a string.
var = "I Like  programming"
index = var.find("  ")
print("The double spaces is at index ",index)

#4-Replace the double space from problem 3 with single spaces.
new_string = var.replace("  "," ")
print(new_string)

# 5- Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry, this python course is nice. Thanks!"
new_letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(new_letter)



