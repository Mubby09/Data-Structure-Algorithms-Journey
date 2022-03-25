class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x , y])
            
        result = []
        heapq.heapify(minHeap)
        while k > 0:
            distance, x ,y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1
            
        return result