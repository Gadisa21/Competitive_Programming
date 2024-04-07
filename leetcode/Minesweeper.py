class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        if board[click[0]][click[-1]]=="M":
            board[click[0]][click[-1]]="X"
            return board

        direction=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        def inbound(row,col):
            return (0<=row<len(board)) and (0<=col<len(board[0]))
        
        def dfs(row,col):

            cntm=0
            for x,y in direction:
                new_row=x+row
                new_col=y+col
                if inbound(new_row,new_col) and board[new_row][new_col]=="M":
                    cntm+=1
            
            if cntm!=0:
                board[row][col]=str(cntm)
            else:
                board[row][col]="B"
                for x,y in direction:
                    new_row=x+row
                    new_col=y+col
                    if inbound(new_row,new_col) and board[new_row][new_col]=="E":
                        dfs(new_row,new_col)
   
        dfs(click[0],click[-1])
        return board
        