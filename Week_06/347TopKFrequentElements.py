import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = dict()
        result = list()

        # count occurences of each number in nums
        # key = num
        # value = occurence of num
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        # sort occurences from least to most common
        hq = []
        for num, occur in dic.items():
            heappush(hq, (occur, num))

        # Find the 3 largest elements
        maxi = heapq.nlargest(k, hq)

        for tup in maxi:
            result.append(tup[1])

        return result