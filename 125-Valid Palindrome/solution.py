class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Keeping only alphanumeric characters and conversion to lower case for uniformity

        ''' indexing from start, indexing from end - 
        if mismatch return false, else continue
        if both indexes become equal and length odd, IS PAL
        if difference between indexes is of 1 and length is even, IS PAL'''

        s = [character.lower() for character in s if character.isalnum()] 
        s_len = len(s)
        is_odd = s_len % 2 == 1 

        lr_index = 0
        rl_index = s_len - 1

        is_pal = True

        end_condition = s_len <= 1

        while (not end_condition):
            if (is_odd):

                if (lr_index == rl_index):
                    end_condition = True

                elif (s[lr_index] != s[rl_index]):
                    is_pal = False
                    break

                else:
                    lr_index += 1
                    rl_index -= 1

            elif (not is_odd):

                if (lr_index - rl_index == 1):
                    end_condition = True

                elif (s[lr_index] != s[rl_index]):
                    is_pal = False
                    break

                else:
                    lr_index += 1
                    rl_index -= 1

        return is_pal



          
        