class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        max_same = 0
        res = 0
        left = 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            max_same = max(max_same, char_count[s[right]])

            while (right - left + 1) - max_same > k:
                char_count[s[left]] -= 1
                left += 1
            
            res = max(res, (right - left + 1 ))
        return res
        