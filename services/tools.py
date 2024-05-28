"""
Tools to be used by Agents handling different tasks
"""

import loguru


def create_file(data, filename: str):
    """
    create file from text input
    :return:
    """
    with open(f'{filename}.txt', 'w') as f:
        # Define the data to be written
        # data = ['This is the first line', 'This is the second line', 'This is the third line']
        # Use a for loop to write each line of data to the file
        for line in data:
            f.write(line + '\n')
            # Optionally, print the data as it is written to the file
            print(line)


def split_text(input_string, max_length=2000):
    """
    Split text till it is less than 2000
    """

    substrings = []
    start = 0
    end = max_length

    while start < len(input_string):
        substrings.append(input_string[start:end])
        start = end
        end += max_length

    return substrings
