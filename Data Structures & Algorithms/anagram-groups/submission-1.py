class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_char = [0]*26
        anagram_index = {}
        for anagram in strs:
            for char in anagram :
                i_alphabet = ord(char) - ord('a')
                anagram_char[i_alphabet] += 1
            anagram_index[tuple(anagram_char)] = [anagram] + anagram_index.get(tuple(anagram_char),[]) 
            anagram_char = [0]*26
        return list(anagram_index.values())
            
