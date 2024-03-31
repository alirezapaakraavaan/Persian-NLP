def remove_punctuations(no_latin_data):
    no_punc_data = ""
    unwanted_punc = ['"',"'",'=','@','&','%','.',',',':','\\','$','^','<','>','!','?','{','}',';','\n','\t','(',')'
                     ,'[',']','/','*','+','#','\u200c','\ufeff','-','_','|']

    for punc in unwanted_punc:
        no_punc_data = no_latin_data.replace(punc, "")

    return no_punc_data
