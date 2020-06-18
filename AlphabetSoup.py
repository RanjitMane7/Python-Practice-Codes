'''
Problem Statement : Alphabet Soup

Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.

'''

def AlphabetSoup(string):
    op = []
    i = 0
    q = ''

    size = len(string)

    while i < size :
        op += string[i]
        i += 1

    op.sort()

    #r = 'A'

    #while i < size :
    #    r += str(op[i])
    #    i += 1

    return q.join(op)

# keep this function call here
print AlphabetSoup(raw_input())
