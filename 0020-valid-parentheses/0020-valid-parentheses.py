class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char in '([{':
                st.append(char)
            else:
                if not st:
                    return False
                top = st.pop()
                if char == ')' and top != '(':
                    return False
                if char == ']' and top != '[':
                    return False
                if char == '}' and top != '{':
                    return False
        return len(st) == 0

# Example usage:
s = "()"
solution = Solution()
result = solution.isValid(s)
print(result)  # Expected output: True