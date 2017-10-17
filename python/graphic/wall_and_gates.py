'''
You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

'''
cc = 'INF'
# cc = 9999


def allsAndGates(rooms):
    visited = [[False] * len(rooms[0]) for _ in range(len(rooms))]
    def dfs(m, n, distance):
        if 0 <= m < len(rooms) and 0 <= n < len(rooms[0]):
            if not visited[m][n]:
                visited[m][n] = True
                if rooms[m][n] == cc:
                    rooms[m][n] = distance
                elif rooms[m][n] == -1:
                    return
                elif distance < rooms[m][n]:
                    rooms[m][n] = distance
                dfs(m - 1, n, distance + 1)
                dfs(m + 1, n, distance + 1)
                dfs(m, n - 1, distance + 1)
                dfs(m, n + 1, distance + 1)

                visited[m][n] = False

    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                dfs(i, j, 0)

def dfs_allsAndGates1(rooms):
    pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(m, n):
        for i in range(4):
            x = m + pos[i][0]
            y = n + pos[i][1]
            if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]):
                if rooms[x][y] == cc:
                    rooms[x][y] = rooms[m][n] + 1
                    dfs(x, y)
                elif rooms[x][y] > rooms[m][n] + 1:
                    rooms[x][y] = rooms[m][n] + 1
                    dfs(x, y)
    def dfs2(m, n, distance):
        for i in range(4):
            x = m + pos[i][0]
            y = n + pos[i][1]
            if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]):
                if rooms[x][y] == cc:
                    rooms[x][y] = distance + 1
                    dfs2(x, y, distance + 1)
                elif rooms[x][y] > distance + 1:
                    rooms[x][y] = distance + 1
                    dfs2(x, y, distance + 1)

    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                # dfs(i, j)
                dfs2(i, j, 0)


def bfs_allsAndGates(rooms):
    queue = []
    def bfs():
        while queue:
            x, y, distance = queue.pop(0)
            if x - 1 >= 0 and rooms[x- 1][y] == cc:
                rooms[x - 1][y] = rooms[x][y] + 1
                queue.append((x - 1, y, distance + 1))
            if x + 1 < len(rooms) and rooms[x + 1][y] == cc:
                rooms[x + 1][y] = rooms[x][y] + 1
                queue.append((x + 1, y, distance + 1))
            if y - 1 >= 0 and rooms[x][y - 1] == cc:
                rooms[x][y - 1] = rooms[x][y] + 1
                queue.append((x, y - 1, distance + 1))
            if y + 1 < len(rooms[0]) and rooms[x][y + 1] == cc:
                rooms[x][y + 1] = rooms[x][y] + 1
                queue.append((x, y + 1, distance + 1))

    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                queue.append((i, j, 0))
    bfs()

def bfs_allsAndGates2(rooms):
    queue = []
    def bfs():
        while queue:
            vals = queue.pop(0)
            for v in vals:
                x, y, distance = v
                if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]):
                    temp = []
                    if rooms[x][y] == cc:
                        rooms[x][y] = distance
                        temp.append((x - 1, y, distance + 1))
                        temp.append((x + 1, y, distance + 1))
                        temp.append((x, y - 1, distance + 1))
                        temp.append((x, y + 1, distance + 1))
                    else:
                        rooms[x][y] = min(rooms[x][y], distance)

                    if temp:
                        queue.append(temp)

    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                temp = []
                temp.append((i - 1, j, 1))
                temp.append((i + 1, j, 1))
                temp.append((i, j - 1, 1))
                temp.append((i, j + 1, 1))
                queue.append(temp)
    bfs()


a = [[cc, -1, 0, cc],
     [cc, cc, cc, -1],
     [cc, -1, cc, -1],
     [0, -1, cc, cc]]

# allsAndGates(a)
# print a

bfs_allsAndGates(a)
print a

# yet_allsAndGates2(a)
# print a

# dfs_allsAndGates1(a)
# print a
