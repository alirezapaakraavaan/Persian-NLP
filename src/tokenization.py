from nltk.tokenize import word_tokenize
import nltk

def tokenization(clean_data):
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('perluniprops')
    nltk.download('nonbreaking_prefixes')
    nltk.download('wordnet')
    nltk.download('universal_tagset')
    nltk.download('tagsets')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('universal_tagset')
    tokens = word_tokenize(clean_data)

    return tokens, len(tokens)