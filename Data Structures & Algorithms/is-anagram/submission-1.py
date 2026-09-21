class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counts1 = {}

        for char in s:
            counts1[char] = counts1.get(char, 0) + 1


        counts2 = {}

        for char in t:
            counts2[char] = counts2.get(char, 0) + 1

        for char in t:
            if char not in counts1 or counts1[char] != counts2[char]:
                return False
        
        return True