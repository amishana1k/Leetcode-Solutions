class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        for i in nums:
            if c[i]==1:
                return i

        