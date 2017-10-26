'''
394. Decode String

TAG: Google

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s:
            def recursion_solution():
                l = len(s)
                def recursion(i):
                    val = ''
                    while i < l:
                        if '0' <= s[i] <= '9':
                            n = ''
                            while '0' <= s[i] <= '9':
                                n += s[i]
                                i += 1
                        elif s[i] == '[':
                            i += 1
                            temp, i = recursion(i)
                            val += int(n) * temp
                        elif s[i] == ']':
                            i += 1
                            return val, i
                        else:
                            val += s[i]
                            i += 1
                    return val, i
                return recursion(0)[0]
            def stack_solution():
                i, l = 0, len(s)
                num_stack = []
                res_stack =[]
                val = ''
                while i < l:
                    if '0' <= s[i] <= '9':
                        n = ''
                        while '0' <= s[i] <= '9':
                            n += s[i]
                            i += 1
                        num_stack.append(n)
                    elif s[i] == '[':
                        res_stack.append(val)
                        val = ''
                        i += 1
                    elif s[i] == ']':
                        left_val = res_stack.pop()
                        num = num_stack.pop()
                        val = left_val + val * int(num)
                        i += 1
                    else:
                        val += s[i]
                        i += 1
                return val
            return stack_solution()
        return ''