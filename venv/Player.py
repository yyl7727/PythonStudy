import Class

operation = int(input())

if operation == 1:
    try:
        num = int(input())
    except:
        print("请输入一个整数")
    while True:
        flag = int(Class.Collatz(num))
        if flag != 1:
            num = flag
            print(flag)
        else:
            print(flag)
            break

elif operation == 2:
    spam = ['yyl', 'zxy', 'yyl', 'zxy']
    print(Class.ListToString(spam))

elif operation == 3:
    Class.beautifulprint()

elif operation == 4:
    Class.Dictionary(2)

elif operation == 5:
    Class.stringexcerise()