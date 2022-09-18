from copy import deepcopy
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        memory = {}
        width = len(board[0])
        height = len(board)
        marked = [[False] * width for x in range(height)]
        def helper(x, y, word):
            if word == "":
                return True
            elif x >= height or x < 0 or y >= width or y < 0 :
                return False
            elif word[0] != board[x][y]:
                return False
            elif marked[x][y]:
                return False
            else:
                newword = word[1:]
                marked[x][y] = True
                if (helper(x-1, y, newword) or helper(x+1, y, newword)
                        or  helper(x, y - 1, newword) or helper(x, y + 1, newword)):
                    return True
                else:
                    marked[x][y] = False
                    return False
        
        for x in range(len(board)):
            for y in range(len(board[x])):
                if helper(x, y, word):
                    return True
        return False
        
        