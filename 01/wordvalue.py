from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return f.read().splitlines()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[letter] for letter in word.upper() if str.isalpha(letter)])

def max_word_value(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    score_to_word = {calc_word_value(word):word for word in words}
    return score_to_word[max(score_to_word)]

if __name__ == "__main__":
    pass # run unittests to validate
