class Solution:
    def exist(self, board, word):
        
        def dfs(row, col, index):
            if index == len(word):
                return True

            # This would be to ensure that the index is within bounds
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or word[index] != board[row][col] or board[row][col] == "#":
                return False 

            # Sets the current value within the dfs traversal to # so we know that its visited
            board[row][col] = "#"

            # Checks to see which path is true: left, right, top, down
            res = (dfs(row-1, col, index + 1) or 
                    dfs(row+1, col, index + 1) or 
                    dfs(row, col-1, index + 1) or 
                    dfs(row, col+1, index + 1))

            # 
            board[row][col] = word[index]

            return res

        # Loop through the whole board which is a 2D array
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if dfs(row, col, 0):
                    return True

        return False
