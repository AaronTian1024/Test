# 阶加函数
def fact(a):
    sum = 0
    for i in range(a):
        sum += ( i + 1 )
    return sum
# print(fact(100))


# 判断是否为三角数
def San(num):
    while num!=0:
        if num < 0:
            return 1        # 输入的不是正数

        elif num > 0:
            for j in range(num):
                if (num == fact(j + 1)):
                    return 2        # 是三角数
            else:
                return 3        # 不是三角数
    else:
        return 4        # 退出


number = int(input("请输入一个数："))
while (San(number) != 4):
    if (San(number) == 1):
        number = int(input("请重新输入一个大于0的数："))
        San(number)
    elif (San(number) == 2):
        print("%d是三角数" % number)
        number = int(input("请输入下一个数："))
        San(number)
    elif (San(number) == 3):
        print("%d不是三角数" % number)
        number = int(input("请重新输入一个数："))
        San(number)
else:
    print("退出")