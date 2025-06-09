def clean_log(input_file, output_file):
    with open(input_file,'r') as infile , open(output_file,'w') as outfile:
        for line in infile:
            cleaned = line.strip()
            if cleaned:
                outfile.write(cleaned+'\n')


clean_log("/Users/srisairakeshnakkilla/Python/data/log.txt","/Users/srisairakeshnakkilla/Python/data/cleaned_log.txt")

# summarize json data

import json
def summarize_metrics(json_file):
    with open(json_file,'r') as j:
        data = json.load(j)
        print(f"data: {data}")

        temps = [entry["cpu_temp"] for entry in data]
        freqs = [entry["cpu_freq"] for entry in data]

        print("Average temp: ", sum(temps)/len(data))
        print("Max Frequency: ", max(freqs))

summarize_metrics("/Users/srisairakeshnakkilla/Python/data/metrics.json")