import re

def validBraces(string):
    brackets = ['()', '{}', '[]'] 
    string = re.sub('[^\(\)\{\}\[\]]', '', string)
    while any(x in string for x in brackets): 
        for br in brackets: string = string.replace(br, '')
    return True if len(string) == 0 else False

string = r'hi(hi)()'
print(validBraces(string))




