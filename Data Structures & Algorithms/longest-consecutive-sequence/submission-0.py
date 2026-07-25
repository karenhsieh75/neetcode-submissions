class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_count = 0
        
        for n in nums:
            if n - 1 in nums_set: # not the begin of the sequence
                continue

            cur_count = 1
            while n + cur_count in nums_set:
                cur_count += 1
            
            if cur_count > longest_count:
                longest_count = cur_count
        
        return longest_count
                
            
