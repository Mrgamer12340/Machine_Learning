number = int(input("Enter a number:"))
if number % 2 ==0:
    print("Even")
else:
     print("odd")

username = input("Enter Username: ")
if not username == "admin":
     print("warning")
else:
    print("Welcome Admin")

password = input("Enter the password: ")

if not  password:
    print("Enter Again")
else:
     print("Welcome")

age = int(input("Enter Your age : "))
if not age >= 18:
    print("Access Denied")
else:
     print("Granted")

number = int(input("ENter a Number :"))
if not (number % 2 == 0  and number % 3 == 0):
     print("okay")
else:
     print("Not okay")

name = input("ENter your name :")
if name and name.startswith("A"):
   print("Valid")
else: 
   print("Not Valid")


username = input("Enter Username :")
password = input("Enter Password :")
if username == "admin":
    print("Welcome Admin")
elif password == "1233":
    print("login Sucessfull")
else:
    print("login FAiled")