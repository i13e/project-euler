class Solution:
    def multiplesOf(self, nums: list, limit: int):
        return set([i for i in range(limit) if any([not i % n for n in nums])])

    def test(self):
        assert sum(self.multiplesOf([3, 5], 1000)) == 233168


Solution().test()

factors = input("Enter factors: ").split()
limit = int(input("Enter limit: "))

# print(list(Solution().multiplesOf([int(f) for f in factors], limit)))
print("Sum:", sum(Solution().multiplesOf([int(f) for f in factors], limit)))
