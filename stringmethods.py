
#Print the first character and the last character.
#Print the 7th character (be careful with counting from 0).
#Print Python using slicing.
#Print Programming using slicing.
#Print the last 3 characters using a negative index.
#Print the whole string reversed.
s = "Python Programming"
print(f"first character {s[0]} and last character {s[-1]}")
print(f"the seventh character will be {s[7]}")
print(f"by using slicing we will get {s[0:6]}")
print(f"by slicing we get {s[7:]}")
print(s[-1:-3:-1])
print(f"if whole string is reversed we get {s[::-1]}")
#Print every 2nd character of s, starting from the first.
#Print the length of s. (Count the space too.)
#Print the last character of s without using -1. (Hint: use len().)
print("step()")
print(f"2nd characters: {s[::2]}")
print("the length of s:",len(s))
print(s[len(s)-1])