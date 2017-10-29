'''
TAG: Google
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
'''
def yet_addBoldTag2(s, dict):
    if s and dict:
        bold = [False] * len(s)
        for word in dict:
            lw = len(word)
            for i in range(len(s) - lw + 1):
                if s[i:i + lw] == word:
                    for j in range(i, i + lw):
                        bold[j] = True
        i = 0
        ret = ''
        while i < len(s):
            if bold[i]:
                ret += '<b>'
                while i < len(s) and bold[i]:
                    ret += s[i]
                    i += 1
                ret += '</b>'
            else:
                ret += s[i]
                i += 1
        return ret

def yet_addBoldTag(s, dict):
    if s and dict:
        l = len(s)
        pos_list = []
        for word in dict:
            lw = len(word)
            for i in range(l - lw + 1):
                if s[i:i + lw] == word:
                    pos_list.append((i, i + lw - 1))
        k = pre = 0
        lp = len(pos_list)
        ret = ''
        while k < lp:
            start, end = pos_list[k]
            ret += s[pre:start]
            while k + 1 < lp and pos_list[k + 1][0] <= end + 1:
                end = max(end, pos_list[k + 1][1])
                k += 1
            ret += ('<b>' + s[start:end + 1] + '</b>')
            pre = end + 1
            k += 1
        ret += s[pre:]
        return ret


def addBoldTag(s, dict):
    l = len(s)
    dict_set = set(dict)
    pos_list = []
    for i in range(l):
        for j in range(i, l):
            if s[i:j + 1] in dict_set:
                pos_list.append((i, j))

    k = pre = 0
    lp = len(pos_list)
    ret = ''
    while k < lp:
        start, end = pos_list[k]
        ret += s[pre:start]
        while k + 1 < lp and pos_list[k + 1][0] <= end + 1:
            end = max(end, pos_list[k + 1][1])
            k += 1
        ret += ('<b>' + s[start:end + 1] + '</b>')
        pre = end + 1
        k += 1
    ret += s[pre:]
    return ret


print addBoldTag('abcxyz123', ["abc","123"])
print addBoldTag('aaabbcc', ["aaa","aab","bc"])
print '---------'
print yet_addBoldTag('abcxyz123', ["abc","123"])
print yet_addBoldTag('aaabbcc', ["aaa","aab","bc"])
print '---------'
print yet_addBoldTag2('abcxyz123', ["abc","123"])
print yet_addBoldTag2('aaabbcc', ["aaa","aab","bc"])

