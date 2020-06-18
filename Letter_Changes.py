'''
Problem Statement : Letter Changes

Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
'''

def LetterChanges(str):

    s=len(str)
    i = 0
    p = ''
    while i < s :

        a = ord(str[i])
        if a < 65 or (a > 90 and a < 97) or a > 122 :
            p += str[i]
            i += 1
            continue

        if ord(str[i]) == 32:
            p += ' '
            i += 1
            continue

        r = chr(ord(str[i]) + 1)
        if r in ['i','o','e','a','u'] :
            p += chr(ord(str[i]) - 31)
        else :
            p += r

        i += 1
    #p = chr(ord('a') - 32)
    return p

# keep this function call here
print LetterChanges(raw_input())
