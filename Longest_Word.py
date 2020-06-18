'''
Problem Statement : Longest Word

Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
'''

def LongestWord(sen):

    i = 0
    j = 0
    count = 0
    maxcount = 0
    op = ''
    size = len(sen)

    while i < size:

        q = sen[i]

        while ('A' <= sen[i] <= 'Z') or ( 'a' <= sen[i] <= 'z' ) :

            count += 1

            if count > maxcount :
                maxcount = count
                op += sen[i]
                last = i

            if i+1 == size:
                break

            i += 1

        count = 0
        i += 1

    #op = sen.substr()
    #return last
    return sen[ last-maxcount + 1 : last+1 ]

# keep this function call here

