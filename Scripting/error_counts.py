def error_counts(filename):
    error_counts = {}
    with open(filename,'r') as f:
        for line in f:
            # if 'ERROR' or 'Error' in line:
            #     parts = line.strip().split('ERROR')
            # if len(parts) > 1:
            #         message = parts[1].strip()
            #     else:
            #         message = line.strip()
            if 'error' in line.lower():
                idx = line.lower().find('error')
                message = line[idx + len('error'):].strip()
                
                
                if message in error_counts:
                    error_counts[message] +=1
                else:
                    error_counts[message] = 1
    return error_counts

if __name__ == "__main__":
    filename = "/Users/srisairakeshnakkilla/Python/data/error_counts_log.txt"
    counts = error_counts(filename)
    for error_msg in counts:
        print(f"{error_msg}: {counts[error_msg]}")