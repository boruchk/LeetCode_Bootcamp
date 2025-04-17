class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = dict()


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        trie = TrieNode()

        # add all words from wordDict into a trie
        for word in wordDict:
            self.insert(trie, word)

        check = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or check[i - 1]:
                cur = trie
                for j in range(i, len(s)):
                    char = s[j]
                    if char not in cur.children:
                        break
                    
                    cur = cur.children[char]
                    if cur.is_word:
                        check[j] = True

        return check[-1]


    def insert(self, root, word):
        cur = root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word = True