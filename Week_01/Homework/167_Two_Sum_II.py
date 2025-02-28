class Solution(object):
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # brute force would be to check each element, then check each succeeding element to see if they add to target
    # instead, use 2-pointer method:

    left = 0
    right = len(numbers)-1

    while left < right:
      if numbers[left] + numbers[right] < target:
        left += 1
      elif numbers[left] + numbers[right] > target:
        right -= 1
      elif numbers[left] + numbers[right] == target:
        break

    return [left+1, right+1]