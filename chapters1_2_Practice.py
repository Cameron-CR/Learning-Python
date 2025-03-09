print("Please enter two numbers")
number1 = input()
number2 = input()

print("The Sum of your inputs is: " + str(int(number1) + int(number2)))
print("The difference of your inputs is: " + str(int(number1) - int(number2)))
print("The product of your inputs is: " + str(int(number1) * int(number2)))
print("The quotient of your inputs is: " + str(int(number1) / int(number2)))


#problem 4 and 5
count = 10
while count > 0:
    print(count)
    count -= 1

print("Blast Off")




#Problem 6 - Pass word checker

correctPass = "PythonRocks"
print("Please enter your password")
password = input()
while password != correctPass:
        print("Please enter your password")
        password = input()
        if password == correctPass:
            print("logging you in...")
            break
                
