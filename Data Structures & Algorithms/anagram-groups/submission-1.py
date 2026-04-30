class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      lookup = defaultdict(list)

      for s in strs:
         count = [0] * 26
         for char in s:
            count[ord(char) - ord('a')] += 1
         lookup[tuple(count)].append(s)
      
      return list(lookup.values())


