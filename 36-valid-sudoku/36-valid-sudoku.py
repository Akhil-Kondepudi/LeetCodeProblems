class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for x in range(9)]
        col = [set() for x in range(9)]
        box = [set() for x in range(9)]      
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] != ".":
                    val = board[x][y]
                    
                    if val in row[x]:
                        return False
                    elif val in col[y]:
                        return False
                    elif val in box[(x / 3 + 1) + ((y/3) * 3) - 1]:
                        return False
                    else:
                        row[x].add(val)
                        col[y].add(val)
                        box[(x / 3 + 1) + ((y/3) * 3) - 1].add(val)
        return True