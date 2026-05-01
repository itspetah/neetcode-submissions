class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        biggest = -1
        for num in arr[::-1]:
            ans.append(biggest)
            biggest = max(num, biggest)
        return ans[::-1]
