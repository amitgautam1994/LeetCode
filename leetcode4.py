def findTheDifference(s,t) -> str:
    #         diff = ""
    #         if len(s) != len(t):
    #             if len(s) > len(t):
    #                 return s[len(t):]

    #             elif len(t) > len(s):
    #                 return t[len(s):]

    #         return 0
    dict1 = {}
    dict2 = {}

    for i in s:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    for j in t:
        if j not in dict2:
            dict2[j] = 1
        else:
            dict2[j] += 1

    for key in dict2:
        if key not in dict1:
            return key
        elif dict2[key] != dict1[key]:
            return key



print(findTheDifference("abcd", "abcde"))