"""
Напишите программу для перевода из римских цыфр в арабские
"""
def romanOrInt(string):
    roman = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4,
            'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400,'CM':900}
    i = 0
    num = 0
    while i < len(string):
        if i + 1 < len(string) and string[i:i + 2] in roman:
            num += roman[string[i:i + 2]]
            i += 2
        else:
            num += roman[string[i]]
            i += 1
    print(num)

if __name__ == "__main__":
    romanOrInt(input())