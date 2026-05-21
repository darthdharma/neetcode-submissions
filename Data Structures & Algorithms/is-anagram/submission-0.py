# If two strings are anagrams, they must contain exactly the same characters with the same frequencies.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)