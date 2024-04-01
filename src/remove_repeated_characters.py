import nltk
import re
from nltk.corpus import wordnet


class RepeatReplacer():
    def __init__(self):
        # The beginning and the end char of word can be anything, but there must be a repeated character in the middle
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)') 
        self.repl = r'\1\2\3' # 1: start chars + a char, 2: middle char, 3: end chars

    def replace(self, word):
        if(wordnet.synsets(word)): 
            return word # if the word was in wordnet returns that word.
            
        repl_word = self.repeat_regexp.sub(self.repl, word) # Delete a repeated character
        if(repl_word != word): 
            return self.replace(repl_word) # Recursive function
        else: 
            return repl_word # The word is not in word net


def remove_repeted_characters(tokens):
    nltk.download("wordnet")
    replacer = RepeatReplacer()

    clean_repeat_tokens = []
    for token in tokens:
        clean = replacer.replace(word=token)
        clean_repeat_tokens.append(clean)
        if clean != token: print(token, "=> clean: ", clean)

    return clean_repeat_tokens, len(clean_repeat_tokens)