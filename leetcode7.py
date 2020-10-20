def romanToInt(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if s == "":
        return 0

    ans = 0
    prev = values.get(s[0])
    for num in s:
        ans += values.get(num)
        if prev < values.get(num):
            ans -= 2 * prev
        prev = values.get(num)


    return ans

print(romanToInt("IV"))