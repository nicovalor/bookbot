from stats import count_words, character_times, sorted_dictionary
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    characters = character_times(book)
    ordered_characters = sorted_dictionary(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dic in ordered_characters:
            print(f"{dic['name']}: {dic['num']}")
    print("============= END ===============")



main()