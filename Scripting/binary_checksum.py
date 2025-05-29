def even_parity_count(filename):

    count=0
    with open(filename,'r') as file:
        for line in file:
            bits = line.strip()
            if bits.count('1') %2 ==0:
                count+=1
    return count


print(even_parity_count("/Users/srisairakeshnakkilla/Python/data/binary.txt"))