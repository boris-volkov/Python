import re
import os

file_directory = '/home/boris/Documents/Books/temp/'
head_que = 'Produced by'
tail_que = 'End of the Project Gutenberg EBook'

for subdir, dirs, files in os.walk(file_directory):
    for filename in files:
        if filename.endswith(".txt"):
            with open(subdir + '/' + filename, 'r+') as file:
                book_as_string = file.read()
                try:
                    cleaned = re.search('Produced by(.+?)End of the Project Gutenberg EBook', book_as_string).group(1)
                except AttributeError:
                    # head_que, tail_ que not found in the original string
                    cleaned = book_as_string  # apply your error handling
                file.write(cleaned)
            continue
        else:
            continue


#    start_index = book_as_string.index(head_que)
#   end_index = book_as_string.index(tail_que)
#  book_as_string = book_as_string(start_index:end_index)