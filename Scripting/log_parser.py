def count_log_levels(filename):
    counts = {'INFO':0,'WARNING':0,'ERROR':0}
    with open(filename,'r') as file:
        for line in file:
            if 'INFO' in line:
                counts['INFO']+=1
            elif 'WARNING' in line:
                counts['WARNING']+=1
            elif 'ERROR' in line:
                counts['ERROR']+=1
    return counts

print(count_log_levels("/Users/srisairakeshnakkilla/Python/data/log.txt"))