class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        x=[]
        for i in range(len(sentences)):
            s1=sentences[i].split()
            c=len(s1)
            x.append(c)
        return max(x)