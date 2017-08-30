#Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#word1 and word2 may be the same and they represent two individual words in the list.

def shortestDistance(nums, word1, word2):
    if nums:
        m = n = -1
        ret = len(nums)
        for i in range(len(nums)):
            if nums[i] == word1:
                m = i
                if n != -1:
                    ret = min(ret, abs(m - n))
            elif nums[i] == word2:
                n = i
                if m != -1:
                    ret = min(ret, abs(m - n))
        return ret


def yet_shortestDistance(nums, word1, word2):
    pre, pre_i = '', -1
    m = len(nums)
    same = word1 == word2
    for i in range(len(nums)):
        if same:
            if nums[i] == word2:
                if pre_i != -1:
                    m = min(m, abs(i - pre_i))
                pre_i = i
        else:
            if nums[i] == word1 or nums[i] == word2:
                if pre and pre != nums[i]:
                    m = min(m, abs(i - pre_i))
                pre = nums[i]
                pre_i = i
    return m


# print shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice')
print shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'makes')
print yet_shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'makes')
print yet_shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes')
