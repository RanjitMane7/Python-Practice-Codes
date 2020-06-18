''' 
Problem Statement : Chessboard Traveling
Have the function ChessboardTraveling(str) read str which will be a string consisting of the location of a space on a standard 8x8 chess board with no pieces on the board along with another space on the chess board. The structure of str will be the following: "(x y)(a b)" where (x y) represents the position you are currently on with x and y ranging from 1 to 8 and (a b) represents some other space on the chess board with a and b also ranging from 1 to 8 where a > x and b > y. Your program should determine how many ways there are of traveling from (x y) on the board to (a b) moving only up and to the right. For example: if str is (1 1)(2 2) then your program should output 2 because there are only two possible ways to travel from space (1 1) on a chessboard to space (2 2) while making only moves up and to the right.

'''

count = 0
def ChessboardTraveling(str): 
#str = str
#print(bstr)
    start = int(str[1]),int(str[3])
    dest = int(str[6]),int(str[8])
    m,n = start
    
    '''
    print("m,n", m,n)
    print("start", start)
    print("dest", dest)
    '''
    
    if start == dest :
        return 0
    
    def traverse(m,n):
        global count
        
        if (m,n+1) != (dest[0],dest[1]) and n+1 <= dest[1] : #UP
            #print("UP : ", m, n+1)
            traverse(m,n+1)
        else :
            if (m,n+1) == (dest[0],dest[1]) :
                count += 1
                #print("UP Count : ", m, n+1)
                #print("count : ", count)
                return 0
                
        if (m+1,n) != (dest[0],dest[1]) and m+1 <= dest[0] : #RIGHT
            #print("RIGHT : ", m+1, n)
            traverse(m+1,n)
        else :
            if (m+ 1,n) == (dest[0],dest[1]) :
                count += 1
                #print("RIGHT Count : ", m+1, n)
                #print("count : ", count)
                return 0
                
    traverse(start[0],start[1])
    
    return count

# keep this function call here  
print ChessboardTraveling(raw_input())
