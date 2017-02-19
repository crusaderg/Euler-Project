MAX_ROW    = 20
MAX_HEIGHT = 20

grid = [[1 for i in range(0, MAX_ROW + 1)] for j in range(0,MAX_HEIGHT + 1)]

for i in reversed(range(MAX_ROW - 1)):
    for j in reversed(range(MAX_HEIGHT - 1)):
        grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

paths = 1.0

for i in range(MAX_ROW):
    paths *= (2 * MAX_ROW) - i;
    paths /= i + 1;

print(paths)