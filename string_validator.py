if __name__ == '__main__':
    s = input()
    # shortcut using `any` function
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))

    # Time ==> O(N), takes 5N steps
    # Space ==>O(1), takes only 5 boolean regardless of string size

    # line_1, line_2, line_3, line_4, line_5 = False, False, False, False, False
    # for i in range(len(s)):
    #     if s[i].isalnum():
    #         line_1 = True
    #     if s[i].isalpha():
    #         line_2 = True
    #     if s[i].isdigit():
    #         line_3 = True
    #     if s[i].islower():
    #         line_4 = True
    #     if s[i].isupper():
    #         line_5 = True
    #
    # print(line_1)
    # print(line_2)
    # print(line_3)
    # print(line_4)
    # print(line_5)


    # Using ASCII table is pure madness in python

    # for i in range(len(s)):
    #     if (ord(s[i])>47 and ord(s[i])<58) or (ord(s[i])>64 and ord(s[i])<91) or (ord(s[i])>96 and ord(s[i])<123):
    #         line_1 = True
    #     if (ord(s[i])>64 and ord(s[i])<91) or (ord(s[i])>96 and ord(s[i])<123):
    #         line_2 = True
    #     if (ord(s[i])>47 and ord(s[i])<58):
    #         line_3 = True
    #     if (ord(s[i])>96 and ord(s[i])<123):
    #         line_4 = True
    #     if (ord(s[i])>64 and ord(s[i])<91):
    #         line_5 = True
    #
    # print(line_1)
    # print(line_2)
    # print(line_3)
    # print(line_4)
    # print(line_5)