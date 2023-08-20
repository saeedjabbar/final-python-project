import csv
import os


def read_data(file_path):
    test_data_directory = "../test_data/"
    relative_filename = test_data_directory + file_path # ../test_data/filename_random.csv
    current_directory = os.path.dirname(__file__)
    destination_file = os.path.join(current_directory, relative_filename)

    # Create an empty list to store rows
    rows = []
    # Open the CSV file
    data_file = open(destination_file, 'r')
    # Create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # Skip the headers
    next(reader)
    # Add rows from reader to rows list
    for row in reader:
        rows.append(tuple(row))
    return rows
