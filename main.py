#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = [] #creates a list instead of string("")

for char in range(1, nr_letters + 1): #need +1 to make th erange include the number that the user inputed. Remember that when using range the second number isn't included.
  password_list.append(random.choice(letters)) #using .append adds the random choice of letters to the list that we just created

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

#print(password_list)
random.shuffle(password_list) #once we have the full list created with numbers, letters, and symbols use random.shuffle to randomly shuffle the list we created.
#print(password_list)

password = "" #create variable to start off as empty string
for char in password_list: #this changes the list into a string
  password += char #adds the char form the list we generated into the password string variable we just created

print(f"Your password is: {password}")
