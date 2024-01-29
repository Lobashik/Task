class Solution:
    def reverseWords(s: str) -> str:
        l = s.split()
        s = ''
        for i in l:
            s = s + ' ' + i[::-1]
        return s


if __name__ == "__main__":
    print(Solution.reverseWords(input()))