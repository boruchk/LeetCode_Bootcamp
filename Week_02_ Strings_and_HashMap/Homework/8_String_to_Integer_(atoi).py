class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        neg = 1
        left = 0
        right = 1

        if not s:
            return 0

        if s[0] == '-':
            neg = -1
            left = 1
        
        elif s[0] == '+':
            left = 1

        elif not s[0].isdigit():
            return 0
        
        while right < len(s) and s[right] == '0':
            right += 1

        while right < len(s) and s[right].isdigit():
            right += 1

        result = 0
        for char in range(left, right):
            result = (result * 10) + (ord(s[char]) - ord('0'))
        
        result = result*(neg)
        result = max(-(2**31), min(result, 2**31 -1))

        return result