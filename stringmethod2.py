#Remove the extra spaces from both ends and print the result.
#Print the cleaned text in title case (first letter of each word capital).
#Count how many times the letter o appears in text.
#Replace python with java and print the result.
text = "   i love python programming   "
print(text.strip())
print(text.title())
print(text.count("o"))
text=text.replace("python","java")
print(text)
#Ask the user for a word, then print:
#the word in capital letters
#its length
#its first and last letters
#the word reversed
p=input("enter any word").lower().strip()
print(p.upper())
print("length is",len(p))
print(f"first letter{p[0]} and last letter{p[-1]}")
print("your word in reversed",p[::-1])
#Ask the user for a sentence and print how many words it has. 
#(Hint: split() turns it into a list, and len() works on lists too.)
C=input("enter a sentence bro")
C=C.split()
print(f"your sentemce is {C} and has {len(C)} number of words")