class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        result=""
        for i in range(len(words)):
            if words[i]==words[i][::-1]:
                result=words[i]
                break
        return result
        