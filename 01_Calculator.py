# This is Robo-wiz!! 
# This code is a calculator

print("------------ code # 1 ------------")

def is_number(num):
  try:
    float(num)
    return True
  except ValueError:
    return False

# this part of the code asks the user for the operator
symbol = input("What operator would you like to use? Please enter one of this symbols: + - * or /  ")
# this checks if the entered symbol is eligible math operator
if symbol != "+" and symbol != "-" and symbol != "*" and symbol != "/":
  print("uh oh... please try again! The symbols are: + - * /")
else:
    # these lines of code asks the user for what numbers do they want to use
    num1 = input("what is your first number? ")
    num2 = input("what is your second number? ")
    # this if statement calls is_numer method and confirms if the inputs are true numbers
    if is_number(num1) and is_number(num2):
        # this changes the inputs to decimals/float    
        num1 = float(num1)
        num2 = float(num2)
        # these if and elif statements add/subtract/multiply/divide the numbers and printing out the answer
        if symbol == "+":
            print("your answer is:",round(num1+num2,5))
        elif symbol == "-":
            print("your answer is:",round(num1-num2,5))
        elif symbol == "*":
            print("your answer is:",round(num1*num2,5))
        elif symbol == "/":
            print("your answer is:",round(num1/num2,5))
    # if one of the inputs contains letters/string, then this code will print and program will be terminated
    else:
        print("Your input can not be used in an real equation, maybe you added an extra charecter? Please try again with numbers (positive or negative)")