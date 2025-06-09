
# read a verilog file and list out all the module names
import os 
import re
def list_module_names(filename):
    module_names=[]
    with open(filename,'r') as f:
        for line in f:
            match = re.match(r'\s*module\s+(\w+)',line)
            if match:
                module_names.append(match.group(1))
    return module_names


print(list_module_names("/Users/srisairakeshnakkilla/EDA/verilog/SV_UVM_practice/SV/Verilog/count_ones_zeros.sv"))

# Extract errors and warnings 

def extract_err(log_path,out_path):
    with open(logpath,'r') as log_file, open(out_path,'w') as out_file:
        for line in log_file:
            if 'ERROR' in line or 'WARNING' in line:
                out_file.write(line)

# count the number of testcases

def test_cases_count(log_path):
    passed = failed =0
    with open(log_path,'r') as file:
        if 'TESTCASE PASS' in line:
            passed+=1
        elif 'TESTCASE FAIL' in line:
            failed+=1
        
    return passed,failed

# list all relevant files in the directory

def list_files(directory):
    relevant_files =[]

    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(('.sv','.v','.log')):
                relevant_files.append(os.path.join(root,file))
    return relevant_files



