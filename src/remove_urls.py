import re

def remove_urls(no_unicode_data):
    no_url_data = re.sub(r'https?://[a-zA-Z0-9\.\/\-_?=;&]*', '', no_unicode_data)

    return no_url_data