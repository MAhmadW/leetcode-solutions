class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        nums_len = len(nums) 

        # Remove all val in nums by iteration - simply popping works

        curr_idx = 0

        while (curr_idx < len(nums)):

            if nums[curr_idx] == val:
                nums.pop(curr_idx )
                continue
            
            curr_idx += 1

        # Yield number of elements in nums != val
        return curr_idx 
            

        
        