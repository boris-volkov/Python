from collections import Counter
import csv
import os

throw_aways = "0123456789-.;_(){}[]\\/:?!\",\n"


def eat_file():
    directory = '/home/boris/Documents/Books/'
    book = 'buckley_cancer'

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


# puts all books into a single array
def eat_folder():
    file_directory = '/home/boris/Documents/Books/'
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

    print(str(len(book_strings_array)) + "   books")
    big_string = ''.join(book_strings_array)

    for char in throw_aways:
        big_string = big_string.replace(char, ' ')
    big_string = big_string.lower()

    print(str(len(big_string)) + "  characters")
    word_list = big_string.split()

    counts = Counter(word_list).most_common()

    print(str(len(counts)) + "   unique words")

    with open(file_directory + title + '_counts.csv', "w", newline='') as my_csv:
        writer = csv.writer(my_csv)
        writer.writerows(counts)


eat_folder()