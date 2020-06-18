'''
Problem Statement : Eight Queens

Have the function EightQueens(strArr) read strArr which will be an array consisting of the locations of eight Queens on a standard 8x8 chess board with no other pieces on the board. The structure of strArr will be the following: ["(x,y)", "(x,y)", ...] where (x,y) represents the position of the current queen on the chessboard (x and y will both range from 1 to 8 where 1,1 is the bottom-left of the chessboard and 8,8 is the top-right). Your program should determine if all of the queens are placed in such a way where none of them are attacking each other. If this is true for the given input, return the string true otherwise return the first queen in the list that is attacking another piece in the same format it was provided.

For example: if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] then your program should return the string true. The corresponding chessboard of queens for this input is below (taken from Wikipedia).
'''


'''
#Input:"(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"
#Output:"(2,1)"



inn = [[2,1], [4,3], [6,3], [8,4], [3,4], [1,6], [7,7], [5,8]]

 for i,j in inn :
	print('---',i,j)
	t = 1
	for k in range(min(i,j),9) :
		if [i+t,j] in inn or [i,j+t] in inn or [i+t,j+t] in inn :
			print('Culprit',i,j)
			exit()
		print('====k',k)
		t += 1
'''


def EightQueens(strArr):
    inn = []
    for i in strArr:
        temp = []
        for k in i:
            if k.isdigit():
                temp.append(int(k))
        inn.append(temp)
    print(inn)
    
    for (i, j) in inn:
        t = 1
        print(i,j)
        for k in range(min(i, j), 9):
            if [i + t, j] in inn or [i, j + t] in inn or [i + t, j + t] in inn :
                return '(' + str(i) + ',' + str(j) + ')'
            t += 1
    
    return 'true'


# keep this function call here
print(EightQueens(["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"]))
