# my_tuples=(1,3,5)
# print(my_tuples)
# tuples followthe same indexing as lists


# strings
my_str = "hello world"
# print(my_str[3])
# out: l

# print(my_str[3:])
# print(my_str[::-1])
# print(len(my_str))
# print(my_str.count("l"))
# print(my_str.title())
# print(my_str.find("W")) #out: -1 still be
# # strings are immutable so we never actually change the original string but instead generated new strings

# print(my_str.replace("world","friend"))
# print(my_str.split("_"))
# print(my_str.split("l")) # ['he', '', 'o wor', 'd']
# strip removes white spaces
print(my_str.strip())

print(" ".join(["hello","world","join","me"]))

# format string
name="rakesh"
age="26"
city="tempe"
# print("My name is "+ name + " I am " + str(age) + " and I live in "+"Paris")
template_str = "My name is {} I am {} and I live in {}"

template_str.format(name,age,city)
print(template_str)

print(f"My name is {name} I am {age} and I live in {city}")