class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        columns = len(board[0])

        def search(row, col, w_index):
            if w_index == len(word):
                return True
            if row < 0 or row >= rows:
                return False
            if col < 0 or col >= columns:
                return False
            if board[row][col] != word[w_index]:
                return False
            
            current_char = board[row][col]
            board[row][col] = "#"

            found = (
                search(row+1, col, w_index+1)
                or search(row-1, col, w_index+1)
                or search(row, col+1, w_index+1)
                or search(row, col-1, w_index+1)
            )

            board[row][col] = current_char

            return found
        for row in range(rows):
            for col in range(columns):
                if board[row][col] == word[0]:
                    if search(row, col, 0):
                        return True
        return False