class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        largest_str = strs[0]

        for word in strs:
            if len(word) < len(largest_str):
                largest_str = word

        i = 0

        while i < len(largest_str):
            for word in strs:
                if word[i] != largest_str[i]:
                    return largest_str[:i]

            i += 1
        return largest_str


