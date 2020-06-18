'''
Problem Statement : Vowel Square
Have the function VowelSquare(strArr) take the strArr parameter being passed which will be a 2D matrix of some arbitrary size filled with letters from the alphabet, and determine if a 2x2 square composed entirely of vowels exists in the matrix. For example: strArr is ["abcd", "eikr", "oufj"] then this matrix looks like the following:

a b c d
e i k r
o u f j

Within this matrix there is a 2x2 square of vowels starting in the second row and first column, namely, ei, ou. If a 2x2 square of vowels is found your program should return the top-left position (row-column) of the square, so for this example your program should return 1-0. If no 2x2 square of vowels exists, then return the string not found. If there are multiple squares of vowels, return the one that is at the most top-left position in the whole matrix. The input matrix will at least be of size 2x2.

'''

# Input:"aqrst", "ukaei", "ffooo"
# Output:"1-2" 'row-column'


vowel = ['a','i','o','e','u']
temp = []
ls2 = []

strArr = ["one","two","three"]

for i in strArr :
	for j in i :
		temp.append(j)
	ls2.append(temp)
	temp = []

print('ls2 is', ls2)

#ip2 = ["aqrst", "ukaei", "ffooo"]
#inn = [['a','q','r','s','t'], ['u','k','a','e','i'], ['f','f','o','o','o']]
#inn = [['g','g'], ['f','f']]
#inn = [['a','b','c','d'], ['e','i','k','r'], ['o','u','f','j']]

#inn = [['o','n','e'],['t','w','o'],['t','h','r','e','e']]

inn = ls2
flag = 1

for i in inn :
    for j in i :
        if j in vowel :
            if inn[inn.index(i) + 1][i.index(j)] in vowel and \
               i[i.index(j)+1] in vowel and \
               inn[inn.index(i) + 1][i.index(j)+1] in vowel :
                print('Bingo ',inn.index(i),i.index(j))
                flag = 0
                exit()
if flag :
    print('Not found')
