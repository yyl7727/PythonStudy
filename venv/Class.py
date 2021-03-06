# 编写一个名为 collatz()的函数，它有一个名为 number 的参数。如果参数是偶数，
# 那么 collatz()就打印出 number // 2，并返回该值。如果 number 是奇数，collatz()就打
# 印并返回 3 * number + 1。
def Collatz(number):
    if number==1:
        return number
    elif number%2==0:
        return number/2
    else:
        return 3*number+1


# 传入一个列表，返回一个字符串，该字符串包含所
# 有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。
def ListToString(spam):
    str2=''
    for i in range(len(spam)-1):
        str2=str2+str(spam[i])+','
    str2=str2+'and '+spam[-1]
    return str2


# 漂亮的输出一个桃心
def beautifulprint():
    grid = [[' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'O', 'O', ' ', ' ', ' '],
            ['O', 'O', 'O', 'O', ' ', ' '],
            ['O', 'O', 'O', 'O', 'O', ' '],
            [' ', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', ' '],
            ['O', 'O', 'O', 'O', ' ', ' '],
            [' ', 'O', 'O', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ']]

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i], end='')
        print()


# 字典练习
def Dictionary(op):
    dic = {'rope': 1, 'torch': 5, 'gold': 200}
    num = 0
    if op == 1:
        print('Inventory:')
        for i, j in dic.items():
            print(str(j)+' '+str(i))
            num += j
        print('Total number of items:' + str(num))
    # 假设征服一条龙的战利品表示为这样的字符串列表：
    # dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    # 更新到背包
    elif op == 2:
        dragonloot = ['gold', 'dagger', 'gold', 'gold', 'ruby']
        for index in range(len(dragonloot)):
            if dragonloot[index] in dic:
                dic[dragonloot[index]] += 1
            else:
                dic[dragonloot[index]] = 1
        print('Inventory:')
        for i, j in dic.items():
            print(str(j) + ' ' + str(i))
            num += j
        print('Total number of items:' + str(num))


def stringexcerise():
    print('请输入一个字符串（仅限英文字符串）')
    teststr = input()
    if not teststr.isalpha():
        print('你输入的什么jb？')
    else:
        print('你输入的很棒！')