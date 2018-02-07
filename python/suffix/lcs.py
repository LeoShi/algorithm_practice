def LCS(s1, s2):
    def build_suffix(s):
        suffix = [(s[i:], i) for i in range(len(s))]
        ss = sorted(suffix)
        return [w[1] for w in ss]

    def lcs(i, j):
        count = 0
        while i < l and j < l and s[i] == s[j]:
            i += 1
            j += 1
            count += 1
        return count
    s = s1 + '#' + s2
    l = len(s)
    suffix_array = build_suffix(s)
    idx_of_sharp = s.index('#')
    max_len, start_idx = 0, -1
    for i in range(l - 1):
        if (suffix_array[i] - idx_of_sharp) * (suffix_array[i + 1] - idx_of_sharp) < 0:
            current_len = lcs(suffix_array[i], suffix_array[i + 1])
            if max_len < current_len:
                max_len = current_len
                start_idx = suffix_array[i]
    return s[start_idx:start_idx + max_len]

print LCS('abcdefd', 'srgcdefq')