# Convert integer to roman numerals

def intToRoman(num):
    digit = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX','V', 'IV', 'I']

    romanDigits = ''
    k = 0

    while num>0:
        for i in range(num//digit[k]):
            romanDigits += roman[k]
            num -= digit[k]

        k+=1

    return romanDigits


print(intToRoman(1423))

