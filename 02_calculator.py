#let's define the basic operations first:
#addition
def addition(x,y):
 return x+y
#subtraction
def subtraction(x,y):
 return x-y
#multiplication
def multiplication(x,y):
 return x*y
#division
def division(x,y):
 return x/y

#now let's define user options:
print("Please select an operation:\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")

#let the user choose an option aaand get his numbers:
while True:
 choice = input("Which operation do you want to do? (1, 2, 3, 4): ")
 if choice in ('1','2','3','4'):
  try:
   num1 = float(input("Your first number: "))
   num2 = float(input("Your second number: "))
  except ValueError:
   print("I cannot do this if you don't cooperate :( Choose a number please.")
   continue

  if choice == '1':
   print("The result of adding your numbers is ", addition(num1,num2))

  elif choice == '2':
   print("The result of subtracting your numbers is ", subtraction(num1,num2))
  
  elif choice == '3':
   print("The result of multiplying your numbers is ", multiplication(num1,num2))

  elif choice == '4':
   print("The result of dividing your numbers is ", division(num1,num2))
  
   #now let's get the user option of another calculation:
  next_one = input("Want to do more calculations?: (yes/no): ")
  if next_one == "no":
    break
 else:
   print("It's not that hard to choose a number between 1 and 4... try again")






  