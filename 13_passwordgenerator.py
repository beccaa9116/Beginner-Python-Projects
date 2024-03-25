import random
import string

def password_generator(min_length, numbers=True, special_characters=True):
 letters = string.ascii_letters
 digits = string.digits
 special = string.punctuation

 characters = letters
 if numbers:
  characters += digits

 if special:
  characters += special

 password = ""
 meets_criteria = False
 has_number = False
 has_special = False

 while not meets_criteria or len(password) < min_length:
  new_character = random.choice(characters)
  password += new_character

  if new_character in digits:
   has_number = True
  elif new_character in special:
   has_special = True

  meets_criteria = True
  if numbers:
   meets_criteria = has_number
  elif special_characters:
   meets_criteria = meets_criteria and has_special

 return password

min_length = int(input("Enter the minimum length: "))
has_number = input("Should the password include numbers? (y/n): ").lower() == "y"
has_special = input("Should the password include special characters? (y/n): ").lower() == "y"

pwd = password_generator(min_length, has_number, has_special)
print("This is the generated password: ", pwd)