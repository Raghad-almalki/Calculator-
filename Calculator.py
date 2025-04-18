# Simple Calculator

num1 = float(input("enter first num: "))
op = input("enter operation: ")
num2 = float(input("enter num2: "))
if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "*":
  print(num1 * num2)
elif op =="/":
  print(num1 / num2)
else:
  print("please enter valid operation")
