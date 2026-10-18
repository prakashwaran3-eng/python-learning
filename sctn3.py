#Question 1
#Convert the string "123" to an integer, add 7 to it, and print the result.
string="123"
convert_string=int(string)
print(f"the result is :{convert_string+7}")
#second method 
print("second method ")
string="123"
print("the result will be :",int(string)+7)



print("QUESTION 2")
#Convert the float 9.99 to an int and print it.
# What happens to the decimal part? (Write one comment explaining.)
a=9.99
a=int(a)#here the float value is converted into an integer by using int 
#the deciaml part will cut off 
print(a)


print("QUESTION 3")
#. Convert the integer 0,
#the string "" and the string "hello" to bool and print all three.
a=0
b="hello"
c=""
print(bool(a))
print(bool(b))
print(bool(c))