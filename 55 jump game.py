class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reachable = 0
        for i,step in enumerate(A):
            if reachable < i:
                break
            else:
                reachable = max(reachable, i+step)
        return reachable >= len(A)-1
        
if __name__ == "__main__":
    print Solution().canJump([2,3,1,1,4])
    print Solution().canJump([3,2,1,0,4])
