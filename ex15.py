from sys import argv

script, fileName = argv

txt = open(fileName)

print(f"Here's your file {fileName}:")
print(txt.read())

print("Type the fileName again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
