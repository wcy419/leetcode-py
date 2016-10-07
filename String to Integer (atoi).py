class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        Sign = 1
        i = 0
        sum = 0
        
        while i < len(str) and str[i].isspace():
            i += 1
        if i < len(str) and str[i] == "-":
            Sign = -1
        if i < len(str) and (str[i] == "-" or str[i] == "+"):
            i += 1
        while i < len(str) and str[i].isdigit():
            digit = int(str[i])
            temp = sum*10 + digit
            if INT_MAX >= temp:
                sum = temp
            else:
                if Sign == -1:
                    return INT_MIN
                else:
                    return INT_MAX
            i += 1
        return Sign*sum
            
            
if __name__ == "__main__":
    print Solution().myAtoi("") 
    print Solution().myAtoi("-+1")
    print Solution().myAtoi("2147483647") 
    print Solution().myAtoi("2147483648") 
    print Solution().myAtoi("-2147483648")  
    print Solution().myAtoi("-2147483649") 
