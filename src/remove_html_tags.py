import re

def remove_html_tags(no_urls_data):
    no_html_data = re.sub(r'<[^>]+>', '', no_urls_data)

    return no_html_data