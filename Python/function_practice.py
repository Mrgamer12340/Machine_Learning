# Fahrenheit to Celsius
# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Please Enter the temperature: "))
# print(f"{f_to_c(f)}")

# Pattern
# def pattern(n):
#     if n == 0:
#         return
#     print("*" * n)
#     pattern(n-1)
# n = int(input("Please enter the number: "))
# pattern(n)


# centimeters=inches×2.54
# def i_to_c(inches):
#     return inches * 2.54

# f = int(input("Please enter Inches: "))
# print(f"{i_to_c(f)}")

def multiplay(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
multiplay(6)