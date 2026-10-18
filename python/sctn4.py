#Ask the user for two numbers and print their sum.
a=int(input("enter first number"))
b=int(input("enter second number"))
c=a+b
print("the sum is:",c)


#QUESTION 2
print("finding fahrenheit")
#Ask for a temperature in Celsius and print it in Fahrenheit (F = C * 9/5 + 32).
temp=int(input("enter the temprature in clesius:"))
fahrenheit=temp*9/5 +32
print(fahrenheit)



#QUESTION 3
#Ask for the radius of a circle and print its area (use 3.14159).
r=float(input("enter the radius"))
area=3.14159*r*r
print("the area of the circle ",area)


#last one i am happy because
#so i can rest a while
#, Q13 (the challenge): ask for total seconds (e.g. 3725) and print it as hours : minutes : seconds. For 3725 the output is 1 : 2 : 5.
total = int(input("Enter total seconds: "))

hours = total // 3600
remaining = total % 3600

minutes = remaining // 60
seconds = remaining % 60

print(f"{hours} : {minutes} : {seconds}")