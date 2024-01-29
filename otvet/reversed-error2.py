class Solution:
    def reverseWords(s: str) -> str:
        l = s.split()
        s = ''
        for i in l:
            s = s + ' ' + i[::-1]
        return s


if __name__ == "__main__":
    print(Solution.reverseWords(input()))

"""
Тут сам вывод неправильный, т.к. мы возвращаем s, а у нас в любом случае
из-за выбранного решения будет нулевой элемент пробелом (надо написать return s[1:])
"""