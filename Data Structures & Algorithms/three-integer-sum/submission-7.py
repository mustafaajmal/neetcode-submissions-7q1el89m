class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, item in enumerate(nums):
            if index > 0 and item == nums[index - 1]:
                continue
            
            l, r = index + 1, len(nums) - 1
            while l < r:
                if item + nums[l] + nums[r] > 0:
                    r -= 1
                elif item + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([item, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
