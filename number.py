

'''
    古希腊毕达哥拉斯学派认为“万物皆数”,
    他们常把数描绘成沙滩上的点子或小石子,
    再根据点子或小石子排列的形状把整数进行分类,
    如:1、3、6、10······这些数叫作三角形数(如下图)。
    那么,判断一下 45、456、1830、5050 这四个数中,哪些是三角形数。
     
    需求：判断三角数
'''


# 阶加函数
def fact(a):
    sum = 0
    for i in range(a):
        sum += (i+1)
    return sum
# print(fact(100))


# 判断是否为三角数
def San(num):
    while num==0:
        print("退出")
        break
    else:
        if num<0:
            num = int(input("请重新输入一个大于0的数："))
            San(num)

        elif num>0:
            for j in range(num):
                if (num == fact(j+1)):
                    print("%d是三角数" %num)
                    break
            else:
                print("%d不是三角数" %num)
                number = int(input("请重新输入一个数："))
                San(number)
            number = int(input("请输入下一个数："))
            San(number)

    
    


number = int(input("请输入一个数："))
San(number)


# while(San(number)):
#     number = int(input("请输入下一个数："))
#     San(number)
# else:
#     number = int(input("请重新输入一个数："))
#     San(number)








# if(flag):
#     print("%d是三角数" %num)
# else:
#     print("%d不是三角数" %num)





