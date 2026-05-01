from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = []
        for i in range(k):
            most_frequent = max(counter, key=counter.get)
            ans.append(most_frequent)
            del counter[most_frequent]
        return ans