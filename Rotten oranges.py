class Solution:
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        queue = []

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.pop(0)
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or col < 0 or col == COLS) or grid[row][col] != 1:
                        continue
                    queue.append([row, col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1


grid = [[1, 0, 2], [0, 1, 2], [2, 1, 1]]
obj = Solution()
ans = obj.orangesRotting(grid)
print(ans)
