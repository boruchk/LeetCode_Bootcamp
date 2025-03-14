class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        wordlist = []

        curword = ""

        for char in s:
            if char == " " and curword:
                wordlist.append(curword)
                curword = ""
            elif char == " ":
                curword = ""
            else:
                curword += char

        if not curword == " ":
            wordlist.append(curword)
        
        result = ""
        for word in range(len(wordlist)-1, 0, -1):
            result = result + wordlist[word] + " "
        result = result + wordlist[0]

        return result