import json

config_json_path = 'models/tokenizer_config.json'  
word_index_json_path = 'models/tokenizer_word_index.json'    
output_json_path = 'models/restructured_config.json'


with open(config_json_path, 'r') as config_file:
    existing_config = json.load(config_file)

# Load the word index JSON content
with open(word_index_json_path, 'r') as word_index_file:
    word_index_data = json.load(word_index_file)

# Include the word index data within the configuration
existing_config['word_index'] = word_index_data

# Write the modified JSON content back to the file
with open(output_json_path, 'w') as output_file:
    json.dump(existing_config, output_file, indent=4)

print(f"JSON files restructured and saved to {output_json_path}")
