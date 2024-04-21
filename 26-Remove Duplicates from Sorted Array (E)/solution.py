class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Non decreasing implies increasing implies ascending

        encountered = []

        # Index through nums

        curr_idx = 0

        while(curr_idx < len(nums)):
            
            if not nums[curr_idx] in encountered:
                encountered.append(nums[curr_idx])
                curr_idx += 1
            
            else:
                nums.pop(curr_idx)

        return len(nums)