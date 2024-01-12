def upper_case(words):
    """this should turn a list of words into seperate lines and words turned into uppercase"""
    for word in words:
        print(word.upper())



def first_letter_e(words):
    """this should only return words that start with the letter e"""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())



def print_words(words, must_start):
    """this should take a list of words and list of letters and only print words that start with that letter"""
    for word in words:
        for letter in must_start:
                if word.startswith(letter):
                    print(word.upper())



print_words(["hello", "hey", "goodbye", "yo", "yes",'juan'],['h','g','j'])
