'''
Written under linux, might need modification for other OS
'''

from collections import Counter
import csv
import os
from typing import List, Tuple

# the word counter this program uses is space-delimited so all punctuation marks
# need to be replaced with spaces, here you mark everything that you want replaced

throw_away_chars = "0123456789-.;_<>(){}[]\\/:?!\",\n"

directory = '/home/boris/Documents/Books'
book = 'homer_iliad'


# single file version
def eat_file(dir, text_file):
    """Return a wordcount from a text file.

    The arguments are directory and book title (without extension)
    ex: eat_file('/home/boris/Documents/Books/' , 'homer_iliad')

    Returns a dict with words being mapped to their count within the file
    Sorted descending by count.
    Dict is also saved to a .csv file in the same directory
    """

    directory = dir
    book = text_file

    with open(directory + book + '.txt', 'r') as file:
        book_as_string = file.read().replace('\n', ' ')

    for char in throw_away_chars:
        book_as_string = book_as_string.replace(char, ' ')

    book_as_string = book_as_string.lower()

    print(len(book_as_string))
    word_list = book_as_string.split()

    counts = Counter(word_list).most_common()

    with open(directory + '/' + book + '_counts.csv', "w", newline='') as my_csv:
        writer = csv.writer(my_csv)
        writer.writerows(counts)

    print(len(counts))
    print(counts)


# directory version
def eat_folder(dir, t):
    """
    Return a wordcount for all of the text files in a directory

    The argument a string of the directory containing the files you want to process.
    ex: eat_folder('/home/boris/Documents/Books/')

    Returns a dict mapping words to their total count in all of the text files in dir.
    The result will be a single dict for all of the books combined.
    Not a separate file for each book.

    The os.walk function returns triples
    (dirpath : string,
    dirnames : list of immediate children of dirpath,
    filenames : list of files in dirpath)

    Also writes the dict to a .csv file into the directory passed in.
    """
    file_directory = dir
    title = t
    num_books = 0
    total_counts = Counter()
    for dir, subdirs, files in os.walk(file_directory):
        for filename in files:
            if filename.endswith(".txt"):
                num_books += 1
                with open(dir + '/' + filename, 'r', errors='ignore') as file:
                    book_as_string = file.read().replace('/n', ' ')
                for char in throw_away_chars:
                    book_as_string = book_as_string.replace(char, ' ')
                book_as_string = book_as_string.lower()
                word_list = book_as_string.split()
                current_counts = Counter(word_list)
                total_counts = total_counts + current_counts
                print(num_books)
                continue
            else:
                continue

    print(str(num_books) + " total books")
    print(str(len(total_counts)) + "   unique words")

    total_counts: List[Tuple] = total_counts.most_common()
    total_counts.insert(0 , ('word', 'n'))


    with open(file_directory + "/" + title + '_counts.csv', "w", newline='') as my_csv:
        writer = csv.writer(my_csv)
        writer.writerows(total_counts)

eat_folder("/home/boris/Documents/original" , "my")
