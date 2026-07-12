# Easy
for number in range(50):
    print(number)

for number in range(100):
   if number % 2 == 0:
    print(number)

num = int(input("Enter Number: "))
for i in range(1,11):
   print(f"{num} x {i} = {num * i}")


number = [99,21,43,234]
largest = number[0]
for num in number:
   if num > largest:
      largest = num

print(number,largest) 