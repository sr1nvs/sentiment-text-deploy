import csv
import random
import os

input_csv_file = 'models/data.csv'
output_dir = 'models/splitdata'
os.makedirs(output_dir, exist_ok=True)

train_ratio = 0.8
validation_ratio = 0.1
test_ratio = 0.1

data = []

# Open the input CSV file for reading
with open(input_csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Read the header row

    # Collect all the data from the CSV file
    for row in csv_reader:
        data.append(row)

random.shuffle(data)

total_samples = len(data)
train_size = int(train_ratio * total_samples)
validation_size = int(validation_ratio * total_samples)

# Split the shuffled data into train, validation, and test sets
train_data = data[:train_size]
validation_data = data[train_size:(train_size + validation_size)]
test_data = data[(train_size + validation_size):]

# Write the data to separate CSV files for train, validation, and test sets
def write_csv(filename, data):
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)  # Write the header row
        csv_writer.writerows(data)

train_csv_file = os.path.join(output_dir, 'train.csv')
validation_csv_file = os.path.join(output_dir, 'validation.csv')
test_csv_file = os.path.join(output_dir, 'test.csv')

write_csv(train_csv_file, train_data)
write_csv(validation_csv_file, validation_data)
write_csv(test_csv_file, test_data)

print(f"Data split completed. Train set: {len(train_data)} samples, Validation set: {len(validation_data)} samples, Test set: {len(test_data)} samples")
