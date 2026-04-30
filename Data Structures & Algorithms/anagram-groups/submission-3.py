class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      anagrams = defaultdict(list)
      
      for s in strs:
         buckets = [0] * 26
         for char in s:
            buckets[ord(char) - ord('a')] += 1
         anagrams[tuple(buckets)].append(s)
      return list(anagrams.values())
      

        