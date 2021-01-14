def backtrack(r, c, word, board):
    
    rows=len(board)
    cols=len(board[0])

    #print(word)
    #Check if word has been completely checked
    if len(word)==0:
        return True #Nothing else to be checked

    #Check all the boundary conditions and grid value checks
    if (r<0 or r >=rows) or (c<0 or c>=cols) or (board[r][c]!=word[0]):
        return False

    #Now since the grid letter is same as the first letter in the word, mark it with a special character to avoid confusions during backtracking

    #print(board[r][c])
    temp=board[r][c]
    board[r][c]='*'

    ret=False
    #continue with backtracking for the adjacent cells
    for x,y in [(-1,0),(0,1),(1,0),(0,-1)]:

        ret=backtrack(r+x, c+y, word[1:], board)

        if ret:
            break
    
    #Replace the changed special character cell back to original
    board[r][c]=temp

    return ret

def wordSearch(board, word):

    rows=len(board)
    cols=len(board[0])

    ret=False
    #traverse the grid and check backtrack for each letter
    for r in range(rows):
        for c in range(cols):
            ret=backtrack(r, c, word, board)

            if ret:
                return ret
        
    return ret

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

print(wordSearch(board, word))