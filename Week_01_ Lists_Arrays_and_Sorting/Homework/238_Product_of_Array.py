class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = list()

    total = 1
    totalwz = 1
    
    for i in range(len(nums)):
      if nums[i] == 0:
        totalwz = total
        total = total*nums[i]
      else:
        total = total*nums[i]
        totalwz = totalwz*nums[i]

    for i in range(len(nums)):
      if nums[i] == 0:
        answer.append(totalwz)
      else:
        answer.append(total / nums[i])

    return answer