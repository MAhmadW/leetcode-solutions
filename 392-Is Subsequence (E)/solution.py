class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Index through t, keep finding matches of s until end or subsequence found

        s_index = 0
        t_index = 0

        s_len = len(s)
        t_len = len(t)

        sub_found = not s

        while(not sub_found and t_index < t_len):

            if s[s_index] == t[t_index]:
                s_index += 1 

                sub_found = s_index == s_len

            t_index += 1

        return sub_found
            
        