class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, dic = [], {"(":")","[":"]","{":"}"}
        for p in s:
            if p in dic:
                stack.append(p)
            else:
                if len(stack) == 0 or p!= dic[stack.pop()]:
                    return False
        return len(stack) == 0
if __name__ == "__main__":
    s = "[{}()]"
    print (Solution().isValid(s))
