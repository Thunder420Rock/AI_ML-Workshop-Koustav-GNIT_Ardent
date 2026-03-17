# simple calculator 

print("----------Simple Calculator Program---------------")

num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

print("\n Choose Operations: ")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter your chice (1/2/3/4): ")


if choice == "1":
  print("Result =", num1 + num2)
elif choice == "2":
  print("Result =", num1 - num2)
elif choice == "3":
  print("Result =", num1 * num2)
elif choice == "4":
  print("Result =", num1 / num2)
else:
  print("Invalid Input")
