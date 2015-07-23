def make_acronym(sentence):
    sentence = 'light amplification by the simulated emission of radiation'
    excluded_words = ['by', 'the', 'of']
    acronym = ''.join(word[0] for word in sentence.split(' ') if word not in excluded_words)
    return acronym.upper()

make_acronym('light amplification by the simulated emission of radiation')
 
