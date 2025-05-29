# write a funciton that takes an unsigned integer and returns teh number of 1 bits it has (also known as Hamming weight)

# Input : 9
#  Output : 2

def count_ones(num):
    count =0
    while num:
        num=num & (num-1)
        count+=1
    return count

print(count_ones(9))

# count the number of zeros for a given width

def count_zeros(n,width):
    return width - count_ones(n)
    # return i

print(f"count zeros:",count_zeros(9,32)) 

# find out if the number is power of 2

def power_two(n):
    pow2 = n!=0 and n & (n-1) ==0
    # return n!=0 and n & (n-1) ==0
    return f"{n} is a power of 2 {pow2}"

print(power_two(0))


def return_right_set_pos(n):

    if n ==0:
        return 0
    else:
        return (n & -n).bit_length()

print(return_right_set_pos(4))
    
