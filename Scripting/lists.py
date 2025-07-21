# lists
    # mutable objects
#     # stored in a ordered array
#     # heterogenous objects (int,float,str...)
      #  list_1[included:excluded:optional]

# my_list = ["list",1,True]

# second_list = list("list is an ordered array")
# print(second_list)
# # out:'l', 'i', 's', 't', ' ', 'i', 's', ' ', 'a', 'n', ' ', 'o', 'r', 'd', 'e', 'r', 'e', 'd', ' ', 'a', 'r', 'r', 'a', 'y']

# second_list.remove('i')
# # remove deletes only the first match
# print(second_list)
# # out: ['l', 's', 't', ' ', 'i', 's', ' ', 'a', 'n', ' ', 'o', 'r', 'd', 'e', 'r', 'e', 'd', ' ', 'a', 'r', 'r', 'a', 'y']

# empty_list = []
# print(empty_list)

# empty_list.append("im not an empty list")
# print(empty_list)

# combined_list = my_list + empty_list
# print(combined_list)

# combined_list.extend(empty_list)
# print(combined_list)

# # # out: ['im not an empty list']
# # ['list', 1, True, 'im not an empty list']
# # ['list', 1, True, 'im not an empty list', 'im not an empty list']

# # membership in lists

# print(1 in combined_list)
# print(1 not in combined_list)
# print(combined_list.count(1))

# another_list = ["hello","my","name","list"]
# print(another_list[-2])

# nested_list = [[1,2,3],[4,5,6],[7,8]]
# print(nested_list[1][2])

my_slice = [1,2,3,4,5,6,7,7,8,9,9]
# sliced = my_slice[0:6:2]
# print(sliced)
print(my_slice[4:1:-1])
slice1 = my_slice[3:]
# print(slice1)
 


