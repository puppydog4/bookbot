from collections import Counter
def  main():
    with open("books/frankestein.txt") as f:
        book_contents = f.read()
        books = Counter(char for char in book_contents.lower() if char.isalpha())
        character_count = sorted(books.items(), reverse=True)
        print(character_count)

main()
