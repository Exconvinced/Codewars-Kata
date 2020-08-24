
def pig_it(text):
    char, newText = '', ''
    for i in text:
        if i.isalpha():
            char += i
        elif len(char) > 0:
            newText += char[1:] + char[0] + 'ay' + i
            char = ''
        else:
            newText += i
    if char != '':
        newText += char[1:] + char[0] + 'ay'
    # return newText

    print(newText)


pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !') 


# Nominated best code:

# def pig_it(text):
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in text.split()])