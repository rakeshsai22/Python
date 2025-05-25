# slicing - part of list,tuple,string

# basic syntax 
# sequence [start(inclusive):stop(exclusive):step(optional)]

# Indexing

my_list = [10,20,30]
print(my_list[0])

# 1. Basic slicing
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[0:3]) # output: [0, 1, 2] , but not 3 (index 3 is not inclusive)

# 2. Using a step (skipping elements)
print(f"using steps:",my_list[0:5:2]) # output : using steps: [0, 2, 4] skips every 2nd element

# 3. Using negative indices

print(my_list[-3:-1]) # output : [7, 8]

# 4. omitting start and stop (whole list)
print("whole list",my_list[:]) # output: whole list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 5. Slicing a str
my_str = "hello world 1 2 3"
print(my_str[1:4]) # out: ell ( index 1 to 3 )

# 6. Reversing a Sequence
print(my_list[::-1]) # out: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]