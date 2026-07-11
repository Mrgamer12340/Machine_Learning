number = 100
while number > 0:
   print(number)
   number //= 2
# 
# lower or upercase dono ma kam kra ga 
command = ""
while command.lower() != "quit":
   command = input(">")
   print("Show" , command)


# 
count = 0
for number in range(1 ,10):
   if number % 2 == 0:
      count += 1
      print(number)
print(f"We have {count} even numbers")