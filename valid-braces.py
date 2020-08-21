

def validBraces(string):
    brackets = ['()', '{}', '[]'] 
    while any(x in string for x in brackets): 
        for br in brackets: string = string.replace(br, '')
    return False if len(string) != 0 else True

string = r'()[]{}'
print(validBraces(string))




