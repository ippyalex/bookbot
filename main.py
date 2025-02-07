def word_analysis(book_str):
    '''Returns total number of words
    from a string that represents the
    text contents of a book'''

    return len(book_str.split())

def character_analysis(book_str):
    '''Returns a dictionary of the
    set of unique characters paired
    with how many times they appeared
    in the text contents of a book'''

    book_str = book_str.lower()

    char_list = list(book_str)
    char_set  = set(char_list)
    char_dict = {}

    for char_s in char_set:
        num_appearances = 0

        for char_l in char_list:
            if char_s == char_l:
                num_appearances += 1

        char_dict[char_s] = num_appearances

    return char_dict

def sort_character_rankings(char_tuple):
    '''Returns the ranking of every character
    that the 'sorted' method will use to determine
    in what place it should be arranged in a new
    sorted list'''

    return char_tuple[1]

with open("books/frankenstein.txt") as f:
    book_contents = f.read()
    num_words = word_analysis(book_contents)
    unique_characters = character_analysis(book_contents)

    # Sort characters in descending order of how many times they appeared
    unique_characters = unique_characters.items()
    unique_characters = sorted(unique_characters, reverse=True, key=sort_character_rankings)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for char_stat in unique_characters:
        if char_stat[0].isalpha():
            print(f"The '{char_stat[0]}' character was found {char_stat[1]} times")

    print("--- End report ---")
