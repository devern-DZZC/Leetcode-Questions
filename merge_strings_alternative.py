class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1: 
            return word2
        if not word2: 
            return word1

        minLength = min(len(word1), len(word2))
        ans = ''

        for i in range (minLength):
            ans += word1[i] + word2[i]
        
        if len(word1) > len(word2):
            for i in range(minLength, len(word1)):
                ans += word1[i]
        else:
            for i in range(minLength, len(word2)):
                ans += word2[i]
        
        return ans

"""
Edge Cases:
If word1 null, return word2
If word2 null, return word1

1. Find the shorter string (minLength)
2. Iterate through a loop minLength times and append word1[i] and word2[i] to ans
3. If length of word1 > word2, append the remaining characters of word1 to ans
4. Otherwise, append the remaining characters of word2 to ans

"""


    
    
        
        
