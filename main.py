from stats import (
    count_words,
    characters_count,
    sort_ch
    )
import sys

def main():
    filepath = get_filepath()
    frankenstein_text = get_book_text(filepath)
    ch_count = characters_count(frankenstein_text)
    sorted_ch = sort_ch(ch_count)
    num_words = count_words(frankenstein_text)
    print_report(num_words, sorted_ch, filepath)

def get_book_text(filepath):
    try:
        file_content = ""
        with open(filepath) as f:
            file_content = f.read()
        return file_content
    except OSError as e:
        print(f"Error opening file: {e}")

def print_report(num_words, sorted_ch, book_path):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for item in sorted_ch:
        if item['character'].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")

def get_filepath():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

main()