class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#Hello5#World

        result = ""
        for s in strs:
            result += str(len(s))
            result += "#"
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        
        i = 0
        word_count_str = ""
        result = []

        while i < len(s):
            if s[i] != "#":
                word_count_str += s[i]
                i += 1
            else:
                word_count = int(word_count_str)
                result.append(s[i+1:i+1+word_count])
                i += word_count + 1
                word_count_str = ""
        
        return result
            
