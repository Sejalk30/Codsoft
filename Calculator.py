#Simple Calculator!

def add(x,y):
     return x + y 

def subtract(x,y):
     return x - y 

def multiply(x,y):
     return x * y 

def divide(x,y):
     return x / y 


print("Simple Calculator!")
print("-----------------")
print("Operations:")
print("1.Addition")
print("2.Subtraction")
print("3.Multilication")
print("4.Division")

choice =  input("Enter operation number (1-4):")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if choice == "1":
     result = add(num1, num2)
     operation = "+"

elif choice == "2":
     result = subtract(num1, num2) 
     operation = "-"

elif choice == "3":
     result = multiply(num2, num2) 
     operation = "*"
     
elif choice == "4":
     result = divide(num1, num2)
     operation = "/" 

else:
     print("Invalid choice!")
     exit() 

print("-----------------")
print(f"{num1} {operation} {num2} = {result}")                         