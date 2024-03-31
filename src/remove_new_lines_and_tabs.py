import re

def remove_new_lines_and_tabs(data):
    no_tabs_data = data.replace("\\n", " ") # remove new lines \n
    no_tabs_data = no_tabs_data.replace("\\t", " ") # remove tabs
    no_tabs_data = re.sub(re.compile(r'\s+'), " ", no_tabs_data) # remove white spaces

    return no_tabs_data