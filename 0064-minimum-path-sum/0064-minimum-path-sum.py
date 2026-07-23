class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns = len(grid[0])

        min_sum = [0]*columns
        min_sum[0] = grid[0][0]

        for col in range(1, columns):
            min_sum[col] = (
                min_sum[col-1] + grid[0][col]
            )
        for row in range(1, rows):
            min_sum[0] += grid[row][0]

            for col in range(1, columns):
                min_sum[col] = grid[row][col] + min(
                    min_sum[col], min_sum[col-1]
                )
        return min_sum[-1]