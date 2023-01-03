class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashset = set(s)
        for i in hashset:
            if s.count(i) != t.count(i) or len(s) != len(t):
                return False
        return True
        
