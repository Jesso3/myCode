import csv

def convert_to_csv(input_file, output_file):
    with open(input_file, 'r') as input_file:
        reader = csv.reader(input_file, delimiter=' ')
        data = list(reader)

    with open(output_file, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(data)

    print(f"Conversion complete. CSV file '{output_file}' created.")

# Example usage
input_file_path = 'inventory_input.txt'  # Replace with the path to your input file
output_file_path = 'inventory.csv'  # Replace with the desired path for the output CSV file

convert_to_csv(input_file_path, output_file_path)
