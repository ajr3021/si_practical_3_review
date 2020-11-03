import re
#pytest

#dictionary or set file reading

def unique_words(filename):
    regex = "[\w']+"
    word_dict = dict()
    with open(filename) as the_file:
        for line in the_file:
            line = line.strip().lower()
            for word in line.split(" "):
                word = re.findall(regex, word)
                for element in word:
                    if element in word_dict:
                        word_dict[element] += 1
                    else:
                        word_dict[element] = 1
    return word_dict


def search_word(word_dict):
    """
    A function that prompt the user for a word, and prints out the number of times that word occured
    """
    word = input("Enter a word: ")
    if word in word_dict:
        print(word, "appeared", word_dict[word], "times.")
    else:
        print(word, "appeared 0 times.")

# noun verb analysis

#class stuff