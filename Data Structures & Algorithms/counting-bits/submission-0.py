class Solution:
    def bin(self, n):
        word = ""
        if n > 1:
            word = self.bin(n // 2)
        return word + str(n % 2)

    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n + 1):
            ans = self.bin(i)
            output[i] = sum(int(bit) for bit in ans)
        return output