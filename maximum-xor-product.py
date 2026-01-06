# https://leetcode.com/problems/maximum-xor-product/

'''
a = 12 = 8 + 4 = 1100
b = 5  = 4 + 1 = 0101

1101 xor 0010 = 1111
0101 xor 0010 = 0111

each bit of x should maximize the product of the respective bits of a and b
if a and b differ at bit i, set the bit to 1 on the smaller one (which will multiply with the bigger one)
'''

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        #return self.vlad(a,b,n)

        for i in reversed(range(n)):
            mask = 1 << i
            if a & mask and b & mask:
                # a and b are both 1 for this bit: the bit should be 0, and a and b remain 1
                continue
            elif a & mask:
                pass
                # a = 1, b = 0. we can either flip both bits or leave them as-is.
                # the one that's bigger overall should have this bit as zero,
                # so that the other one can multiply the bigger number.
                if a > b:
                    # flip both bits
                    a ^= mask
                    b |= mask
            elif b & mask:
                # b = 1, a = 0. we should only flip the bits if b > a
                if a < b:
                    # flip both bits
                    a |= mask
                    b ^= mask
            else:
                # a and b are both 0 for this bit: the bit should be 1; so, a and b are flipped to 1
                a |= mask
                b |= mask

        mod = int(1e9) + 7
        return ((a % mod) * (b % mod)) % mod
