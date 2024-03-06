import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
all_problems = 10

def problem_gen():
 left = random.randint(min_operand, max_operand)
 right = random.randint(min_operand, max_operand)
 operator = random.choice(operators)

 expression = str(left) + " " + operator + " " + str(right)
 answer = eval(expression)
 return expression, answer

wrong = 0
input("Press enter to start the challenge (it is timed, hurry up!)")
print("---------------------------------")

start_time = time.time()

for i in range(all_problems):
 expression, answer = problem_gen()
 while True:
  guess = input("Problem number #" + str(i+1) + ": " + expression + " = ")
  if guess == str(answer):
   break
  wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------------------------")
print("Job well done!")
print("You finished in", total_time, "seconds!")




