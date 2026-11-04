class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_index = defaultdict(list)
        for anagram in strs:
            anagram_char = [0]*26
            for char in anagram :
                i_alphabet = ord(char) - ord('a')
                anagram_char[i_alphabet] += 1
            anagram_index[tuple(anagram_char)].append(anagram)
        return list(anagram_index.values())
            
