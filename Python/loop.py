for number in range(1,10,3):
    print("Login" , number  , number  * ".")

# for else
sucessful = True
for number in range(3):
    print("Attempt")
    if sucessful:
        print("Sucessful")
        break

else:
    print("Attempt 3 time and failed")

# for loop
# Loop chalega 3 dafa (attempts)
# Har dafa username/password check honge
# Agar sahi ho toh “Welcome Admin”
# Agar galat ho toh attempt count barhta jayega
# 3 se zyada attempts ho gaye toh “limit reached”
successful = False  # Pehle hi define karo

for number in range(3):  # Max 3 attempts
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    if username == "admin" and password == "1234":
        print("Welcome Admin")
        successful = True
        break
    else:
        print("Invalid credentials. Try again.")

if not successful:
    print("Attempt limit reached")
