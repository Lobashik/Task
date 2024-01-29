#Почему тут нет ошибки?
class Solution2:
    def reverseWords(s: str) -> str:
        l = s.split()
        s = ''
        for i in l:
            s = s + ' ' + i[::-1]
        return s[1:]


if __name__ == "__main__":
    print(Solution2.reverseWords(input()))

#А тут есть?
class Solution1:
    def reverseWords(s: str) -> str:
        l = s.split()
        s = ''
        for i in l:
            s = s + ' ' + i[::-1]
        return s[1:]


if __name__ == "__main__":
    Class = Solution1()
    print(Class.reverseWords(input()))


"""
Тут в первом случае мы вызываем просто статистический метод класса (простыми словами не надо self)
Во втором же случае мы создаем экземпляр класса, что подрузамевает, что мы будем вызывать метод класса,
А у нас нет self (значит это статический метод)
"""