# 1. read and print error lines form log file

def error_lines(log_path):
    with open(log_path,'r') as file:
        for line in file:
            if "ERROR" in line:
                print(line.strip())


log_path = "/Users/srisairakeshnakkilla/Python/data/log.txt"
error_lines(log_path)

# strip() - used to remove the leading and trainling white spaces
    # lstrip() = leading
    # rstrip() = trainling
    # // returns a string

# split() - used to split a string into list // returns a list of strings

#######################################################################################

# 2. rename all .txt files to .bak 
import os
def rename_files(directory):
    for filename in os.listdir(directory):
        print(filename)
        if filename.endswith(".bak"):
            base = os.path.splitext(filename)[0]
            os.rename(os.path.join(directory,filename), 
                os.path.join(directory,base + ".txt"))
directory = "/Users/srisairakeshnakkilla/Python/data"
rename_files(directory)

#######################################################################################

# 3. convert yaml to csv

def yaml_csv(yamlfile,csvfile):
    with open(yamlfile,'r') as yamlf:
        data = yaml.safe_load(yamlf)

    with open(csv_file,'w',new_line='') as csvf:
        writer = csv.DictWriter(csvf, fieldname=['test','inputs','expected'])
        writer.writeheader()
        for entry in data:
            writer.writerow(
                {
                    'test':entry.get('test', ''),
                    'inputs':str(entry.get('inputs', '')),
                    'expected':entry.get('expected', '')
                }
            )

yaml_csv('/Users/srisairakeshnakkilla/Python/data/test_case.yaml','/Users/srisairakeshnakkilla/Python/data/testcase.csv')

