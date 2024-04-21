class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        nums_sum = sum(nums)
        nums_len = len(nums)

        left_index = 0
        right_index = nums_len - 1

        target_met = False
        window_len = nums_len

        if (nums_sum > target):

            while(not target_met):

                print(left_index)
                print(right_index)

                left_val = nums[left_index]
                right_val = nums[right_index]
                
                left_neighbour = nums[left_index - 1]
                right_neighbour = nums[right_index - 1]

                if left_val > right_val:
                    right_index -= 1

                    nums_sum -= right_val
                    target_met = nums_sum < target

                    print('window size is: ',window_len)
                    print(nums_sum)
                    print(target_met)

                    if not target_met:
                        window_len -= 1
                    
                    
                    

                elif right_val > left_val:
                    left_index += 1

                    nums_sum -= left_val
                    target_met = nums_sum < target

                    print('window size is: ',window_len)
                    print(nums_sum)
                    print(target_met)

                    if not target_met:
                        window_len -= 1

                elif (right_index - left_index > 1):
                    
                    if left_neighbour >= right_neighbour:
                        right_index -= 1
                        
                        nums_sum -= right_val
                        target_met = nums_sum < target

                        print('window size is: ',window_len)
                        print(nums_sum)
                        print(target_met)

                        if not target_met:
                            window_len -= 1

                        
                    elif right_neighbour >= left_neighbour:
                        left_index += 1
                        
                        nums_sum -= left_val
                        target_met = nums_sum < target
                        
                        print('window size is: ',window_len)
                        print(nums_sum)
                        print(target_met)

                        if not target_met:
                            window_len -= 1

                else: 
                    
                    window_len = 1
                    break

            return window_len


        elif (nums_sum == target):
            return nums_len

        else:
            return 0
        # If entire array doesn't sum to to target, return 0

        return subarray_len if target_met else 0
        