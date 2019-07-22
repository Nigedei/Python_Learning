# "hi" is same as 'hi'

a = "Hallo"
print(a)    #   --> "Hallo"

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)    #    --> will print the multiple lines

# Strings are Arrays

a = "Hello, World!"
print(a[1])       #    --> "e"
print(b[2:5])     #    --> "llo"

a = " Hello, World! "
print(a.strip())  #     --> "Hello, World!" / Java -> .trim()

print(len(a))     #     --> returns the length
print(a.lower())  #     --> returns text in lower case
print(a.upper())  #     --> returns text in upper case


a = "Hello, World!"
print(a.replace("H", "J"))    #     -->   replace() method replaces a string with another string
print(a.split(","))           #     -->   ['Hello', ' World!']    split() splits string into substrings if it finds instances of the separator


#############################################################################################################################

# combine str and int

age = 23
name = "Nikita"

print("{} {}".format(name, age))      #   -->   "Nikita 23"

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
