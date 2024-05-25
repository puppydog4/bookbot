from collections import Counter
def  main(path_to_file):
    #read file
    with open(path_to_file) as file:
        text = file.read()
        #count number of words
        words = text.split()
        num_words = len(words)
        #count number of letters and return them in a dictionary , all in lowercase
        char_count = Counter(text.lower())
        #print a report of the number of words
        print(f"Number of words: {num_words}")
        #print each letter found as "the "x" character was fond xxx times" only for letters in descending order
        for letter, count in char_count.most_common():
            if letter.isalpha():
                 print(f"The '{letter}' character was found {count} times")

#call the function using books/frankenstein.txt
main("./books/frankestein.txt")
