class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        deletions = 0

        for c in range(m):
            for r in range(1, n):
                if strs[r][c] < strs[r - 1][c]:
                    deletions += 1
                    break
        return deletions
