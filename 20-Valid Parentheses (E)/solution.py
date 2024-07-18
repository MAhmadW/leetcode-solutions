class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_dict = {
            ")":"(",
            "]":"[",
            "}":"{",
        }

        stack = []

        for each in s:
            if each in ['(','[','{']: # Bracket start
                stack.append(each)
            elif each in [')',']','}']: # Bracket end

                if len(stack) and bracket_dict[each] == stack.pop(len(stack) - 1):
                    continue
                else :
                    return False

        
        if len(stack):
            return False
        
        return True