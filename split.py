import epubsplit
import os
import math

MAX_KINDLE_SIZE_BYTES = 50 * 1000 * 1000

def split_epub(filepath, split_count = 0):
    size = os.path.getsize(filepath)
    if split_count == 0 or split_count * MAX_KINDLE_SIZE_BYTES > size:
        split_count = math.ceil(size / MAX_KINDLE_SIZE_BYTES)

    epubsplit.split_epub(filepath, split_count)


    print(split_count, size, size / split_count)

def split_epubs(folderpath):
    pass

if __name__ == "__main__":
    path = "M:\Books\One Piece (Digital) (danke-Empire+Anonymous)"
    for epub in os.listdir(path):
        print(epub, end=": ")
        split_epub(os.path.join(path, epub))
    #split_epub("M:\Books\Tobaku Datenroku Kaiji Kazuya-Hen\Tobaku Datenroku Kaiji - Kazuya-Hen v01.cbz")

    #epubsplit.split_epub(filepath, MAX_KINDLE_SIZE_BYTES)