class Solution(object):
  def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    # sort the array by the start of each element
    # compare end of first element and start of next element, if <, then merge (max end of first and end of next)

    merged = []
    intervals.sort(key = lambda x: x[0])

    prev = intervals[0]

    for interval in intervals[1:]:
      # check if start of this <= end of prev ([1, 4], [2, 9])
      if interval[0] <= prev[1]:
          # make end of prev the max of prev and and this end ([1, 9], [2, 9])
          prev[1] = max(prev[1], interval[1])

      else:
        merged.append(prev)
        prev = interval

    merged.append(prev)
    return merged
