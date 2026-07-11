#if statement
if(29>49):
    print("yes")
else:
    print("No")

    age = int(input("Enter your AGe :"))
    if(age > 18):
        print("Yes")
    else:
        print("You are child") 

# match case statement 
        
a = input("Enter a number: ") 
match a:
    case "1": 
        print("yamin is Present")
    case "2":  
        print("ali is Present")
    case "3":  
        print("raza is Present")
    case "4":  
        print("haider is Present")
    case _:  
        print("No Match found")  

# for loop
for i in range(10):
  print(i + 1)
  a =["yamin" , "ali" , "haider" , "sana"]
for item in a:
  print (item)

# while loop
a = 10
while(a < 20):
    print(a)
    a+=1
        