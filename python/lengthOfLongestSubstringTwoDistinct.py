'''
Tag: Google
Given a string, find the longest substring that contains only two unique characters. For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique character is "bcbbbbcccb".
'''
def lengthOfLongestSubstringTwoDistinct(s, k):
    l = len(s)
    if l <= k:
        return s
    left = 0
    m = {}
    ret_max = 0
    for i in range(l):
        m[s[i]] = m.get(s[i], 0) + 1
        if len(m) > k:
            ret_max = max(ret_max, i - left)
            while len(m) > k:
                val = m[s[left]]
                if val == 1:
                    del m[s[left]]
                else:
                    m[s[left]] -= 1
                left += 1
    return max(ret_max, l - left)

print lengthOfLongestSubstringTwoDistinct("abcadcacacaca", 3)
print lengthOfLongestSubstringTwoDistinct("abaac", 2)