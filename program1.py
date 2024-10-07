class Solution:

    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Edge case: If the grid is empty, return 0
        if not grid or not grid[0]:
            return 0

        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        # Helper function to perform DFS and sink the island
        def dfs(i, j):
            # Check for boundaries and if it's water ('W') or already visited
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 'W':
                return
            
            # Mark the land ('L') as visited by converting it to water ('W')
            grid[i][j] = 'W'

            # Visit all adjacent cells (up, down, left, right)
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        # Iterate over every cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If we find a landmass ('L'), it is a new island
                if grid[i][j] == 'L':
                    island_count += 1  # Found a new island
                    dfs(i, j)  # Sink the island using DFS

        return island_count
