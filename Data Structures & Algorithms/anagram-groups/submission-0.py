class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}

        for word in strs:
            s = str(sorted(word))

            if s not in result:
                result[s] = [word]
            else:
                result[s].append(word)

        return [ value for value in result.values()]