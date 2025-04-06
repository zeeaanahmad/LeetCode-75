# MY BASIC LOGIC
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        if len(word1) == len(word2):
            for i in range(len(word1)):
                 result.append(word1[i]+word2[i])
        elif len(word2) > len(word1):
            diff =len(word1)
            leftover=word2[diff:]
            for i in range(len(word1)):
                result.append(word1[i]+word2[i])
            result.append(leftover)
        elif len(word1) > len(word2):
            diff = len(word2)
            leftover=word1[diff:]
            for i in range(len(word2)):
                result.append(word1[i]+word2[i])
            result.append(leftover)
        
        print(result)
        return ''.join(result)


# AFTER OPTIMISING THE CODE
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = [a+b for a,b in zip(word1,word2)]
        merged.append(word1[len(word2):] or word2[len(word1):])
        return ''.join(merged)
        
        