'''
Problem Statement : Load Balancing

Have the function ScaleBalancing(strArr) read strArr which will contain two elements, the first being the two positive integer weights on a balance scale (left and right sides) and the second element being a list of available weights as positive integers. Your goal is to determine if you can balance the scale by using the least amount of weights from the list, but using at most only 2 weights. For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means there is a balance scale with a weight of 5 on the left side and 9 on the right side. It is in fact possible to balance this scale by adding a 6 to the left side from the list of weights and adding a 2 to the right side. Both scales will now equal 11 and they are perfectly balanced. Your program should return a comma separated string of the weights that were used from the list in ascending order, so for this example your program should return the string 2,6

There will only ever be one unique solution and the list of available weights will not be empty. It is also possible to add two weights to only one side of the scale to balance it. If it is not possible to balance the scale then your program should return the string not possible.

'''



'''
Input:"[3, 4]", "[1, 2, 7, 7]"
Output:"1"

Input:"[13, 4]", "[1, 2, 3, 6, 14]"
Output:"3,6"'
'''


#scale = [13,4]
#weights = [1,2,3,6,14]

#scale = [3, 4]
#weights = [1, 2, 7, 7]

scale = [5, 9]
weights = [1, 2, 6, 7]


if scale[0] > scale[1] :
  higher = scale[0]
  lower = scale[1]
else :
  higher = scale[1]
  lower = scale[0]

if scale[0] == scale[1] :
  print('Already matched')
  
  

for i in weights :
  if lower + i == higher :
    print('Bingo1 :', i)
  elif lower + i < higher :
    for j in weights :
      if lower + i + j == higher and i != j :
        print('Bingo2 :',i,j)
  else : #higher < lower + i
    for j in weights :
      if lower + i == higher + j and i != j:
        print('Bingo3 :',i,j)
