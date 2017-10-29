# coding=utf-8
'''
TAG: Google
Given a string, find the longest substring that contains only two unique characters. For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique character is "bcbbbbcccb".
'''

def lengthOfLongestSubstringTwoDistinct(s, k):
    if s:
        left, l = 0, len(s)
        m = {}
        ret = 0
        for i in range(len(s)):
            m[s[i]] = m.get(s[i], 0) + 1
            if len(m) > k:
                while len(m) > k:
                    if m[s[left]] == 1:
                        del m[s[left]]
                    else:
                        m[s[left]] -= 1
                    left += 1
            ret = max(ret, i - left + 1)
        return ret

def yet_lengthOfLongestSubstringTwoDistinct(s, k):
    '''
    steam input, can not fit memory. better using priority dict like structure
    '''
    m = {}
    smallest_pos, ret = 0, 0
    for i in range(len(s)):
        m[s[i]] = (i, s[i])
        if len(m) > k:
            smallest_pos, key = min(m.values())
            del m[key]
            smallest_pos += 1
        ret = max(ret, i - smallest_pos + 1)
    return ret

print yet_lengthOfLongestSubstringTwoDistinct('abcbbbbcccbdddadacb', 2)

print lengthOfLongestSubstringTwoDistinct('abcbbbbcccbdddadacb', 2)


#minimal spanning tree
# INF = 10000
#
# graph =[[INF,7,4,INF,INF,INF],   #INF代表两点之间不可达
#         [7,INF,6,2,INF,4],
#         [4,6,INF,INF,9,8],
#         [INF,2,INF,INF,INF,7],
#         [INF,INF,9,INF,INF,1],
#         [INF,4,8,7,1,INF]]
#
# visited = [False] * len(graph)
#
#
# def prime(idx):
#     visited[idx] = True
#     distance = [INF] * len(graph)
#     s, index = 0, idx
#     for i in range(len(graph)):
#         distance[i] = graph[idx][i]
#     for i in range(1, len(graph)):
#         minor = INF
#         for j in range(len(graph)):
#             if not visited[j] and distance[j] < minor: #//找到未访问的点中，距离当前最小生成树距离最小的点
#                 minor = distance[j]
#                 index = j
#         visited[index] = True
#         s += minor
#         for j in range(len(graph)):
#             if not visited[j] and distance[j] > graph[index][j]: # //执行更新，如果点距离当前点的距离更近，就更新dist
#                 distance[j] = graph[index][j]
#     print "sum:", s
#
# prime(0)


# def find(arr, target):
#     if arr:
#         left, right = 0, len(arr) - 1
#         while left < right:
#             mid = (left + right) / 2
#             # if arr[mid] >= arr[right]:
#             if arr[mid] < arr[right]:
#                 # right = mid
#                 right = mid - 1
#             else:
#                 # left = mid + 1
#                 left = mid
#         print left
#         return left
#
# # find([1,2,4,7,8,9], 5)
# # find([1,2,4,7,8,9], 6)
# # find([1,2,4,7,8,9], 4)
# # find([1,2,4,7,8,9], 7)
# find([7,8,9, 1,2,4], 7)