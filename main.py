word_count = 0

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = len(text.split())
    print(f"found {word_count} total words")
    #print(text)

if __name__ == "__main__":
    main()