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
        for line in data:
            f.write(line + '\n')
            # Optionally, print the data as it is written to the file
            print(f'create file')


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
