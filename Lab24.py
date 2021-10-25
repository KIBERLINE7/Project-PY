def zd1():
    s1 = ""
    print("Enter string s : ")
    s1 = str(input())
    cnt = 0
    fl = 0

    for sim in s1:
        if sim != " ":
            fl = 1
        elif sim == " " and fl == 1:
            cnt += 1
            fl = 0
    if fl == 1:
        cnt += 1
    print(cnt)


def zd2():
    s1 = ""
    print("Enter string s : ")
    s1 = str(input())

    min_len = 1e8
    cnt = 0

    for sim in s1:
        if sim != " ":
            cnt += 1
        elif sim == " " and cnt != 0:
            min_len = min(min_len, cnt)
            cnt = 0

    if cnt != 0:
        min_len = min(min_len, cnt)

    print("Min len word : " + str(min_len))


def zd3():
    s1 = ""
    print("Enter string s : ")
    s1 = str(input())

    c = ""
    cnt = 0

    for i in range(len(s1)):
        if s1[i] != " ":
            cnt += 1
            if cnt == 1:
                c = s1[i]
            else:
                if cnt != 1 and c == s1[i]:
                    s1 = s1[0:i] + "." + s1[i + 1:len(s1)]
        elif s1[i] == " " and cnt != 0:
            cnt = 0
    print("New string s : " + s1)


def zd4():
    s1 = ""
    print("Enter string s : ")
    s1 = input()
    cnt = 0

    pr = "уеыаоэяиюёУЕЫАОЭЯИЮЁ"

    for sim in s1:
        if sim in pr:
            cnt += 1

    print("Count : " + str(cnt))


def zd5():
    print("Enter string s : ")
    s1 = input()

    fa = 0
    fa1 = 0

    for i in range(len(s1)):
        if s1[i] == "\\":
            fa = i
        elif s1[i] == ".":
            fa1 = i
    print(s1[fa + 1:fa1])


def zd6():
    print("Enter string s : ")
    s1 = input()

    fa_l = -1
    fa = 0
    cnt = 0

    for i in range(len(s1)):
        if s1[i] == "\\":
            fa_l = fa
            fa = i
            cnt += 1
    if cnt == 1 :
        print("\\")
    else :
        print(s1[fa_l + 1:fa])


def zd7():
    print("Enter string s : ")
    s1 = input()
    ans = ""

    if len(s1) == 1:
        ans = s1
    else:
        ans = ans + s1[1::2]
        s1 = s1[len(s1)::-1]
        ans = ans + s1[::2]

    print(ans)


t = 0

while True:
    print("Enter number job or 0 for exit : ")
    t = int(input())
    if t == 1:
        zd1()
    elif t == 2:
        zd2()
    elif t == 3:
        zd3()
    elif t == 4:
        zd4()
    elif t == 5:
        zd5()
    elif t == 6:
        zd6()
    elif t == 7:
        zd7()
    elif t == 0:
        exit()
