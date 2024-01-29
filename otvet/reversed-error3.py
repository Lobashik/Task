class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        s = ''
        for i in l:
            s = s + ' ' + i[::-1]
        return s[1:]


if __name__ == "__main__":
    print(Solution.reverseWords(input()))

"""
Такая запись предполагает, что мы будем вызывать статический метод класса (надо убрать self)
"""