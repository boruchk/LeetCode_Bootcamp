class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # find a letter that is in p
        # check next letters for the length of p
        plen = len(p)
        pdic = {}
        for char in p:
            if char not in pdic:
                pdic[char] = 1
            else:
                pdic[char] += 1
        result = []

        for i in range(len(s)):
            print(s[i])
            if s[i] in pdic:
                anacheck = True
                founddic = {}
                print(i)
                for k in range(i, i+plen):
                    if k >= len(s):
                        anacheck = False
                        break
                    if s[k] not in pdic:
                        anacheck = False
                        print("breaking because s[k] not in pdic, s[k] =", s[k], "and k =", k)
                        break 
                    # if not pdic[s[k]] == 1:
                    #     anacheck = False
                    #     print("breaking because", s[k], "=", pdic[s[k]], "and k =", k)
                    #     break 
                    else:
                        if s[k] not in founddic:
                            founddic[s[k]] = 1
                        else:
                            founddic[s[k]] += 1                    

                for key in founddic.keys():
                    if not founddic[key] == pdic[key]:
                        anacheck = False
                        break

                if not founddic == pdic:
                    anacheck = False
                    print(pdic)
                    print(founddic)

                if anacheck:
                    result.append(i)
                

        return result