#!/usr/bin/python3


import os
from stats import presentation,  get_num_words, test
import sys

def get_book_text():
    #filepath=os.path.join(os.getcwd(),"books/frankenstein.txt")
    #if os.path.isfile(filepath):
    #filepath=sys.argv[1]
   # if len(sys.argv) < 2:
    #    print("python3 main.py <path_to_book>")

    try:
        if os.path.isfile(sys.argv[1]):
            filepath=sys.argv[1]
            with open(filepath, "r") as f:
                 file_contents=f.read()
       # elif len(sys.argv) < 2:
        #    print("Usage: python3 main.py <path_to_book>")
         #   sys.exit(1)
    except IndexError:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    except ValueError:
        print("Value provided is not a path".format(sys.argv[1]))
        sys.exit(1)
    #else:
     #   print("no file found")
    return file_contents

def main():

    print("============ BOOKBOT ============")
    if len(sys.argv) >= 2:
        print("Analyzing book found at {}...".format(sys.argv[1]))
    else:
        print("python3 main.py <path_to_book>")
    text=get_book_text()

    print("----------- Word Count ----------")
    get_num_words(text)

    print("--------- Character Count -------")
    solution=test(text)
    presentation(solution)

    print("============= END ===============")
if __name__ == "__main__":
    main()

