word = input("Enter a word: ")
print("First character:", word[0])
print("Last character:", word[-1])
print("Third character:", word[2])

name = input("Enter your name: ")
print("First 3 letters:", name[3])
print("Last 2 letters:", name[-2:])


sentence = input("Enter a sentence: ")
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

sentence1 = input("Enter a sentence: ")

sentence1 = sentence1.strip()
sentence1 = sentence1.replace(" ", "_")
print("Result:", sentence1)

sentence = input("Enter a sentence: ")
print("Position of 'a':", sentence.find("a"))
print("Number of 'a's:", sentence.count("a"))

values = input("Enter comma-separated values: ")
values = values.split(",")
result = " ".join(values)
print("Result:", result)

