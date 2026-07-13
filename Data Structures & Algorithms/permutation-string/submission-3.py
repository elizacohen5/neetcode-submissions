class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)

        if len(s2) < window_len:
            return False
        
        target = Counter(s1)

        window = Counter(s2[:window_len])

        print(window)
        if window == target:
                return True

        for right in range(window_len, len(s2)):
            left = right - window_len
            
            window[s2[left]] -= 1
            window[s2[right]] += 1
            
            if window[s2[left]] == 0:
                del(window[s2[left]])
            
            if window == target:
                return True
        return False
            
    


        