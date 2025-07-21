# Dsctionaries and Sets

# sequence data types like lists, tuples and strings are ordered. Ordering can be useful in some cases, if your data is sorted or has some ordering

#  dict - unordered, mutable
#         dict is an object thta maps a set of named indices called keys to a set of values 
#         keys re immutable, values are mutable

# my_dict = {
#     "name": "Joe",
#     "age": "10",
#     "city":"Paris"
# }
# print(my_dict)

# print(my_dict["name"])

# # add new items
# my_dict["country"] = "France"

# print(my_dict)

# print("name" in my_dict) # only checks for keys not values 
# print("Joe" in my_dict) # False
# print(my_dict.values()) # prints values
# print(my_dict.items()) # prints out keys and values as tuples

# # table data

# my_table_dict= {
#     "name":["Joe","Bob","Henry"],
#     "age": [10,15,21],
#     "city": ["Paris","tempe","los angeles"]
# }

# print(my_table_dict)

# Sets

# sets are unordered,mutable collections of immutable objects that cannot contain duplicates.
# for storing and data manipulation where each value is unique
import set
my_set={1,2,3,4,5,6,7}
print(my_set)
print(type(my_set))

my_set.add(8)


my_set.remove(2)
print(my_set)

# sets donot support indexing

# membershoip can be checked with in 
print(7 in my_set)

# set operations

set1 = {1,2,3,4}
set2 = {5,6,7,8}

set1.union(set2)
print(set1)

set1.difference(set2) # returns the items from set1 that are'nt in set2
set1.issubset(set2)

my_list = [1,2,3,3,3,4,5,6,6,7]
set(my_list)
print(my_list)
