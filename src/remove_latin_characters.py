import re

def remove_latin_characters(no_html_data):
    no_latin_data = re.sub(r'[a-zA-Z0-9]', '', no_html_data)

    return no_latin_data