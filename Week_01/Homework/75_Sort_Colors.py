class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    left = 0
    right = left

    while right < n:
      if nums[right] == 0:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
      right += 1

    right = left
    while right < n:
      if nums[right] == 1:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
      right += 1

    right = left
    while right < n:
      if nums[right] == 3:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
      right += 1