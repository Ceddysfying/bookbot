import sys
from stats import number_of_words
from stats import number_of_chars
from stats import sort_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv)< 2:
        print("Usage: python3 main.py <path_to_book>")
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = number_of_words(book_text)
    num_chars = number_of_chars(book_text)
    sorted_chars = sort_chars(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            pass
    print("============= END ===============")


main()