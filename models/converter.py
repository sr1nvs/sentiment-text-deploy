import json
import csv

input_jsonl_file = 'models/data.jsonl'
output_csv_file = 'models/data.csv'

with open(input_jsonl_file, 'r') as jsonl_file, open(output_csv_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    for line in jsonl_file:
        data = json.loads(line)
        text = data['text']
        label = data['label']

        # Write the data to the CSV file
        csv_writer.writerow([text, label])

print(f"Conversion from JSONL to CSV completed. Output written to {output_csv_file}")
