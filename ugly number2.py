import heapq

class Solution:
    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        ugly_number = 0

        heap = []
        heapq.heappush(heap, 1)
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            if ugly_number % 2 == 0:
                heapq.heappush(heap, ugly_number * 2)
            elif ugly_number % 3 == 0:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
            else:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
                heapq.heappush(heap, ugly_number * 5)

        return ugly_number
if __name__ == "__main__":

    print Solution().nthUglyNumber(10)
    print Solution().nthUglyNumber(5)
    print Solution().nthUglyNumber(1)
