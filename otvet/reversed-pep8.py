class Solution:
    def reverseWords(self, s: str) -> str:
        line = s.split()
        s = ''
        for i in line:
            s = s + ' ' + i[::-1]
        return s[1:]
