class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        
        letters_in_s = {}
        letters_in_t = {}

        for i in range(len(s)):
            letters_in_s[s[i]] = 1 + letters_in_s.get(s[i],0)
            letters_in_t[t[i]] = 1 + letters_in_t.get(t[i],0)
        return letters_in_s == letters_in_t