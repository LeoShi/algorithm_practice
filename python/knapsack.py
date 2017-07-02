# coding=utf-8
a = [(4, 9), #(size, value) c = 10
(3, 6),
(5, 1),
(2, 4),
(5, 1),
]
b = [  #c = 9
(4, 20),
(3, 6),
(4, 20),
(2, 4),
]
c =[ # c= 10
(2, 6),
(2, 3),
(6, 5),
(5, 4),
(4, 6)]

# pack_size = 10


def knapsack(l, pack_size):
    #dp[i][j] first i items in knapsack which size is j
    dp = [[0 for _ in range(pack_size + 1)] for _ in range(len(l) + 1)]

    for i in range(len(l) + 1):
        for j in range(pack_size + 1):
            if i == 0:
                dp[i][j] = 0
            elif j - l[i - 1][0] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - l[i - 1][0]] + l[i - 1][1])
            else:
                dp[i][j] = dp[i- 1][j]
    # print dp
    return dp[len(l)][pack_size]


def yet_knapsack(l, pack_size):
    dp = [0 for _ in range(pack_size + 1)]
    for i in range(len(l) + 1):
        for j in range(pack_size, -1, -1):
            if i > 0 and j - l[i - 1][0] >= 0:
                dp[j] = max(dp[j], dp[j - l[i - 1][0]] + l[i - 1][1])

    return dp[pack_size]


def bag(l, pack_size):
    res = [[0 for j in range(pack_size + 1)] for i in range(len(l) + 1)]
    for j in range(pack_size + 1):
        res[0][j] = 0
    for i in range(1, len(l) + 1):
        for j in range(1, pack_size + 1):
            res[i][j] = res[i - 1][j]
            if j >= l[i - 1][0] and res[i][j] < res[i - 1][j - l[i - 1][0]] + l[i - 1][1]:
                res[i][j] = res[i - 1][j - l[i - 1][0]] + l[i - 1][1]
    # print res
    return res[len(l)][pack_size]


def show(n, c, w, res):
    print('最大价值为:', res[n][c])
    # x = [False for i in range(n)]
    # j = c
    # for i in range(1, n + 1):
    #     if res[i][j] > res[i - 1][j]:
    #         x[i - 1] = True
    #         j -= w[i - 1]
    # print('选择的物品为:')
    # for i in range(n):
    #     if x[i]:
    #         print('第', i, '个,', end='')
    #         print('')


# print knapsack(a, 3)
# print yet_knapsack(a, 3)
# print bag(a, 3)
print knapsack(a, 3), yet_knapsack(a, 3), bag(a, 3)
print knapsack(a, 10), yet_knapsack(a, 10), bag(a, 10)
print knapsack(b, 9), yet_knapsack(b, 9), bag(b, 9)
print knapsack(c, 10), yet_knapsack(c, 10), bag(c, 10)


