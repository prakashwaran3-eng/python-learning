a=12
b=34
#sum 
c=a+b
print("the sum is :",c)
#subract
c=a-b
print("the subract is :",c)
#divide
c=a/b
print("the divide is :",c)
#floor division
c=a//b
print("the floor division",c)
#reminder 
c=a%b
print("the remainder is: ",c)
#product
c=a*b
print("the productis :",c)
c=a**b
print("a**b :",c)
#swap variables 
a=55
b=88
a,b=b,a # here a = 55,b=88 and after the = it will assign the values to b and a b=55 a=88
print(a,b)
#3rd Questions
a=499.99
total=a*3
print(round(total,2))
# using f string to do operations
# it is very simple and we dont need to use 3rd varible
#  and time sving
a=44
b=87
print(f"sum is {a+b}")