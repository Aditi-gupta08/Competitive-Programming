class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)
        s2 = str(a)
        s2 = s2[2:]
        l = 32 - len(s2)
        s2 = '0'*l + s2

        s2 = s2[::-1]
        return int(s2, 2)