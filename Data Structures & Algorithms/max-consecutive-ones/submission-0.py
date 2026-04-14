class Solution:
    def findMaxConsecutiveOnes(self, nums):
      currentCount = 0
      maxCount = 0
      for num in nums:
        if num == 1:
          currentCount += 1
        else:
          maxCount = max(maxCount, currentCount)
          currentCount = 0
      return max(maxCount, currentCount)
        