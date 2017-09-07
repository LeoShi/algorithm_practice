class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def tire_tree():
            root = {}
            for word in wordDict:
                current = root
                for c in word:
                    current = current.setdefault(c, {})
                current['__end__'] = 'end'
            return root

        root = tire_tree()
        l = len(s)
        cache = {}
        ret = []
        m = {}

        def exist(word):
            if word in cache:
                return cache[word]
            current = root
            for c in word:
                if c in current:
                    current = current[c]
                else:
                    return False
            v = '__end__' in current
            cache[word] = v
            return v

        def bt_without_cache(index, temp):
            if index == l:
                sub_list = ' '.join(temp)
                ret.append(sub_list)
                return
            for i in range(index, l):
                if exist(s[index:i + 1]):
                    bt_without_cache(i + 1, temp + [s[index:i + 1]])

        def bt_with_cache(index):
            if s[index:] in m:
                return m[s[index:]]
            ret = []
            if index == l:
                ret.append('')
                return ret
            for i in range(index, l):
                w = s[index:i + 1]
                if exist(w):
                    sub_list = bt_with_cache(i + 1)
                    for sub in sub_list:
                        ret.append(w + (' ' if sub else '') + sub)
            m[s[index:]] = ret
            return ret

        return bt_with_cache(0)


print Solution().wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print Solution().wordBreak('catsanddog', ["cat","cats","and","sand","dog"])

