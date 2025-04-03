class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = 0
        res = ""

        for char in s:
            if char.isdigit():
                num = (num * 10) + int(char)
            elif char == '[':
                stack.append((num, res))
                res = ""
                num = 0
            elif char == ']':
                curnum, curstr = stack.pop()
                res = curstr + curnum*res
            else:
                res += char
        
        return res