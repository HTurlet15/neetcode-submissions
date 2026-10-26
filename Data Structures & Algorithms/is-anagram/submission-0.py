class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        
        letters_in_s = {}
        letters_in_t = {}

        for i in range(len(s)):
            if s[i] not in letters_in_s :
                letters_in_s[s[i]] = 1
            else : 
                letters_in_s[s[i]] += 1
            
            if t[i] not in letters_in_t :
                letters_in_t[t[i]] = 1
            else :
                letters_in_t[t[i]] += 1
        return letters_in_s == letters_in_t