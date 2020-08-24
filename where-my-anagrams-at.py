def anagrams(word, words):
    copy, theList = word, []
    for char in words:
        charCopy = char
        if len(word) == len(char):
            for i in copy:
                copy = copy.replace(i, '', 1)
                charCopy = charCopy.replace(i, '', 1)
            copy = word
        if charCopy == '':
            theList.append(char)
    print(theList)


# Nominated best code:
# def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
            
        




anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) # => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) # => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) # => []