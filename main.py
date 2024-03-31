from src.load import load
from src.remove_new_lines_and_tabs import remove_new_lines_and_tabs
from src.remove_urls import remove_urls
from src.remove_html_tags import remove_html_tags
from src.remove_latin_characters import remove_latin_characters
from src.remove_punctuations import remove_punctuations
from src.remove_hashtags import remove_hashtags
from src.tokenization import tokenization


data = load('data.csv')
no_tabs_data = remove_new_lines_and_tabs(data)
no_urls_data = remove_urls(no_tabs_data)
no_html_data = remove_html_tags(no_urls_data)
no_latin_data = remove_latin_characters(no_html_data)
no_punc_data = remove_punctuations(no_latin_data)
no_hashtag_data = remove_hashtags(no_punc_data)
clean_data = remove_new_lines_and_tabs(no_hashtag_data)
tokens, tokens_count = tokenization(clean_data)
print(tokens, tokens_count)