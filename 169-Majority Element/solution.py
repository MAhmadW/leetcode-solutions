class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Use dict for occurences

        num_dict = {}

        for num in nums:
            occurences = num_dict.get(num, None)

            if not occurences:
                num_dict[num] = 1
            else:
                num_dict[num] = num_dict[num] + 1

        for num, occurences in num_dict.items():
            if occurences > int(len(nums)/2): 
                return num
        