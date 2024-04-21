class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        # nums array is sorted and unique

        ranges = []

        if not len(nums):
            return []

        previous_num = nums[0]-1

        curr_range_start = nums[0]
        curr_range_end = nums[0]

        # Index through each element in nums

        for num in nums:

            if not previous_num and not previous_num == 0:
                print('a')
                curr_range_start = num
                curr_range_end = num
                previous_num = num

            elif num == previous_num + 1: 
                print('b')
                previous_num = num
                curr_range_end = num

            else:
                if curr_range_start == curr_range_end:
                    print('c')
                    ranges.append(str(curr_range_start))

                    previous_num = num

                    curr_range_start = num
                    curr_range_end = num
                else:
                    print('d')
                    ranges.append(str(curr_range_start)+'->'+str(curr_range_end))
                    previous_num = num

                    curr_range_start = num
                    curr_range_end = num

        if curr_range_start and curr_range_end or (curr_range_start == 0  or curr_range_end == 0):
            if curr_range_start == curr_range_end:
                ranges.append(str(curr_range_start))
            else:
                ranges.append(str(curr_range_start)+'->'+str(curr_range_end))
                previous_num = None

        return ranges

            


        