
print("hello")
number= input("Enter a number: ")
try:
    intnumber = int(number)
    print(f"{number} is an integer")
except:
    print(f"{number} is not an integer")
