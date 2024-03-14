# A simple calculator that can perform basic arithmetic operations

# Define a function that takes two numbers as parameters and returns their sum
def add(num1, num2):
  # Write your code here
  add= num1 + num2
  return(add)

# Define a function that takes two numbers as parameters and returns their difference
def subtract(num1, num2):
  sub= num1 - num2
  return(sub)

# Define a function that takes two numbers as parameters and returns their product
def multiply(num1, num2):
  mult= num1 * num2
  return(mult)

# Define a function that takes two numbers as parameters and returns their quotient
def divide(num1, num2):
  # Write your code here
  div= num1 / num2
  return(div)

# Define a function that takes an operator as a parameter and returns the corresponding function
def get_operation():
  usreoperator= str(input("which operation would u like to perform, add, sub, div, or mutl?: "))
  return(usreoperator)

# Define a function that prompts the user for a number and returns it as a float
def get_number():
  # Write your code here
  num1=float(input("What number would u like: "))

  return(num1)

# Define a function that prompts the user for an operator and returns it as a string
def get_operator():
  num2=int(input("What number would u like to be the operator: "))
  return(num2)

# Define a function that performs a calculation based on the user's input and prints the result

def calculate():
  # Write your code here
  if usreoperator == "add":
    calc=add(num1, num2)

  elif usreoperator == "sub":
    calc=subtract(num1, num2)

  elif usreoperator == "mult":
    calc=multiply(num1, num2)

  else:
    calc=divide(num1, num2)
  return(calc)

# Define a variable that controls the main loop
running = True

# Print a welcome message
print("Welcome to the simple calculator!")
num1=get_number()
num2 =get_operator()
usreoperator= get_operation()
# Start the main loop
while running:
  # Call the calculate function
  print(f'{calculate()} is the answer to {num1} {usreoperator} with {num2}')

  # Ask the user if they want to continue
  answer = input("Do you want to continue? (y/n) ")

  # Check the user's answer
  if answer == "n":
    # Set the running variable to False
    running = False
    # Print a goodbye message
    print("Goodbye!")
  elif answer == "y":
    # Do nothing and continue the loop
    pass
  else:
    # Print an error message
    print("Invalid input. Please enter y or n.")
    