def addTwoNumbers(l1, l2):
    num1 = []
    num2 = []

    for i in l1:
        num1.append(str(i))
    for j in l2:
        num2.append((str(j)))

    num1.reverse()
    num2.reverse()

    n1 = int("".join(num1))
    n2 = int("".join(num2))

    new = str(n1 + n2)

    new = new[::-1]

    lst = []

    for k in new:
        lst.append(int(k))


    print(lst)


addTwoNumbers([2,4,3], [5,6,4])
