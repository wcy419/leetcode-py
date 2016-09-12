class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        jump_count = 0
        reachable = 0
        curr_reachable = 0
        for i, length in enumerate(A):
            if i > reachable:
                return -1
            if i > curr_reachable:
                curr_reachable = reachable
                jump_count += 1
            reachable = max(reachable, i + length)
        return jump_count


    
if __name__ == "__main__":
    print Solution().jump([2,3,3,1,1,4])
    print Solution().jump([3,2,2,0,4])
