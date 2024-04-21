class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Non-decreasing implies increasing implies ascending

        # Dictionary to map occurrences to each element

        num_dict = {}

        # Index through nums

        curr_idx = 0

        while (curr_idx < len(nums)):
            occurences = num_dict.get(nums[curr_idx], None)

            if not occurences: # First occurence
                num_dict[nums[curr_idx]] = 1

            elif occurences == 1:
                num_dict[nums[curr_idx]] = 2

            else:
                nums.pop(curr_idx)
                continue
            
            curr_idx += 1

        return len(nums)

        