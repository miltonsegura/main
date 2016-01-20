def make_acronym(sentence, excluded_words=[]):
    acronym = ''.join(word[0] for word in sentence.split(' ') if word not in excluded_words)
    return acronym.upper()

def main():
    excluded_words = ['by', 'the', 'of']
    sentence = 'light amplification by the simulated emission of radiation'
    make_acronym(sentence, excluded_words)
 
if __name__ == '__main__':
    main()
