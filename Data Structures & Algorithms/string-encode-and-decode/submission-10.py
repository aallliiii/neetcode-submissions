class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + "#" + s
        return encodedString
       
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i<len(s):
            j=i
            while s[j] != "#":
                j = j + 1
            length = int(s[i:j])
            string = s[j+1:j+1+length]
            i = j + 1 + length
            result.append(string)
        return result
    