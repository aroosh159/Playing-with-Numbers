number = int(input("Enter your number"))
temp = number
reversed_number = 0

while temp>0:
    digit = temp % 10
    reversed_number = reversed_number *10 +digit
    temp//=10
if number == reversed_number:
    print(f"{number} is palindore")
else :
    print(f"{number} is not  palindore")