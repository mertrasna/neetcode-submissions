class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        best_streak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_streak += 1
                best_streak = max(best_streak, current_streak)
            else:
                current_streak = 0
        return best_streak
            


            
        