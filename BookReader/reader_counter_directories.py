'''
Written under linux, might need modification for other OS
'''

from collections import Counter
import csv
import os
from typing import List, Tuple

# the word counter this program uses is space-delimited so all punctuation marks
# need to be replaced with spaces, here you mark everything that you want replaced

throw_aways = "0123456789-.;_(){}[]\\/:?!\",\n"


directory = '/home/boris/Documents/Books/'
book = 'homer_iliad'

#single file version
def eat_file(dir , text_file):
    """Return a wordcount from a text file.

    The arguments are directory and book title (without extension)
    ex: eat_file('/home/boris/Documents/Books/' , 'homer_iliad')

    Returns a dict with words being mapped to their count within the file
    Sorted descending by count.
    Dict is also saved to a .csv file in the same directory
    """

    directory = dir
    book = book

    with open(directory + book + '.txt', 'r') as file:
        book_as_string = file.read().replace('\n', ' ')

    for char in throw_aways:
        book_as_string = book_as_string.replace(char, ' ')

    book_as_string = book_as_string.lower()

    print(len(book_as_string))
    word_list = book_as_string.split()

    counts = Counter(word_list).most_common()

    with open(directory + book + '_counts.csv', "w", newline='') as my_csv:
        writer = csv.writer(my_csv)
        writer.writerows(counts)

    print(len(counts))
    print(counts)


# directory version
def eat_folder(dir):
    """
    Return a wordcount for all of the text files in a directory

    The argument a string of the directory containing the files you want to process.
    ex: eat_folder('/home/boris/Documents/Books/')

    Returns a dict mapping words to their total count in all of the text files in dir.
    The result will be a single dict for all of the books combined.
    Not a separate file for each book.

    Also writes the dict to a .csv file into the directory passed in.
    """
    file_directory = dir
    book_strings_array = []
    title = "all"
    for subdir, dirs, files in os.walk(file_directory):
        for filename in files:
            if filename.endswith(".txt"):
                with open(subdir + '/' + filename, 'r', errors='ignore') as file:
                    book_as_string = file.read().replace('/n', ' ')
                for char in throw_aways:
                    book_as_string = book_as_string.replace(char, ' ')
                book_as_string = book_as_string.lower()
                book_strings_array.append(book_as_string)
                continue
            else:
                continue

    print(str(len(book_strings_array)) + '   books')
    big_string = ''.join(book_strings_array)

    for char in throw_aways:
        big_string = big_string.replace(char, ' ')

    big_string = big_string.lower()

    print(str(len(big_string)) + "  characters")
    word_list = big_string.split()

    counts: List[Tuple[str, int]] = Counter(word_list).most_common()

    print( (counts[0][1]*3) / len(big_string) )
    print(str( len(counts)) + "   unique words" )

    print(counts)
    print(type(counts))

    with open(file_directory + title + '_counts.csv', "w", newline='') as my_csv:
        writer = csv.writer(my_csv)
        writer.writerows(counts)


eat_folder('/home/boris/Documents/Books/aristotle/')
