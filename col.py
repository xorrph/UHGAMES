def traverse(board,num,totalA,totalB):
    count = 0 
    temp = board[num][0] 
    start = num 
    side = 0
    board[start][side] = 0
    index  = start + 1 
    while count < temp:
        print(count)
        if count < temp and index <=  len(board)  - 1 and side == 0:
            board[index][side]  = board[index][side]  + 1
            index += 1
            count += 1
        elif count < temp and index == len(board) :
            if side == 0:
                totalA += 1
                side += 1
                index = len(board) -1
            elif side == 1:
                totalB +=1
                side -= 1
                index = 0
            count += 1
        elif count < temp and index >= 0 and side == 1:s
            board[index][side]  = board[index][side]  + 1
            index -= 1
            count += 1
    return board, totalA,totalB
                
        
        
        


board = [[1,4],[2,3]]
board, totalA,totalB = traverse(board,1,0,0)
print(board, totalA,totalB)

# 
# 1 4
# 0 4
#   1
#
