from stats import (get_num_words, get_num_char) 


def get_book_text(book):
    with open(book) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words=get_num_words(text)
    char_output = get_num_char(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book: {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count ---------")
    #print(char_output)

    for char, count in sorted(char_output.items(), key=lambda item: item[1], reverse=True):
        if char.isalpha() == True:
            print(f"{str(char)}: {count}")
        if char.isalpha() == False:
            continue
    print("============= END ===============")

if __name__ == "__main__":
    main()