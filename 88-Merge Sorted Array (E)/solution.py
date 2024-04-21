class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Non decreasing implies increasing implies ascending
        # Are temp variables allowed? Assume YES 

        # Vars for indexing each list
        nums1_index = 0
        nums2_index = 0

        # Var for building nums1
        overall_index = 0

        # Deep copy nums1 into temp
        temp = [element for element in nums1] 

        # Iterate across temp, and num2, adding elements until all exhausted

        while (nums1_index < m or nums2_index < n):

            if (nums1_index == m ):
                nums1[overall_index] = nums2[nums2_index]
                nums2_index += 1
                overall_index += 1

            elif (nums2_index == n ):
                nums1[overall_index] = temp[nums1_index]
                nums1_index += 1
                overall_index += 1

            elif (temp[nums1_index] < nums2[nums2_index]):
                nums1[overall_index] = temp[nums1_index]
                nums1_index += 1
                overall_index += 1
                
            else:
                nums1[overall_index] = nums2[nums2_index]
                nums2_index += 1
                overall_index += 1