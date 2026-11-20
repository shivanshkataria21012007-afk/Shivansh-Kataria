text = "I love python"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
text1= "Shivansh"
print(text1.swapcase())

#string search functions
print(text.find("love"))
print(text.index("love"))

print(text.count("o"))
print(text.startswith("I love"))
print(text.endswith("python"))

#sreing check function

print( 'abc' .isalpha())
print( '123' .isdigit())
print( 'abc123' .isalnum())
print( 'abc123' .isalnum())

#strng modify function
text1 = "   I love python   "
print(text1.replace("python", "java"))

#strip()
text1 = "  Hello  "
newstring = text1.strip()
print(newstring)

newstring1 = text1.lstrip()
print(newstring1)

text = "apple, banana, pineapple, cherry"
fruits = text.split(", ")
