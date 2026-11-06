class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=str(len(strs)) + '.'
        for s in strs:
            encoded += str(len(s)) + '.' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        length = ''
        index = 0
        #Take the number of strings
        while s[index] != '.':
            length += s[index]
            index +=1
        index +=1
        length = int(length)

        string = ''
        decoded = []
        for i_strings in range(length) :
            #Take the length of the following string
            string_length = ''
            while s[index] != '.':
                string_length += s[index]
                index +=1
            index +=1
            string_length = int(string_length)
            #iterate through that string
            for i in range(string_length):
                string += s[i+index]
            index += string_length
            decoded.append(string)
            string = ''
        return decoded
            

