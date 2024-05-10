class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a=""
        while columnNumber > 0:
            a = chr((columnNumber - 1) % 26 + ord('A')) + a
            columnNumber = (columnNumber - 1) // 26
        return a