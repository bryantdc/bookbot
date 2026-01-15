from stats import get_num_words


def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words=get_num_words(text)
    print(f"Found {num_words} total words")

    



if __name__ == "__main__":
    main()