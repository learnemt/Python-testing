import random
import time
try:
    only = []
    i = j = 0
    sTime = eTime = 0.0
    number = int(input("请输入要随机几位："))
    xiao = int(input("请输入最小随机数："))
    da = int(input("请输入最大随机数："))
    isOnly = int(input("请输入是否唯一(1/0)"))
    sTime = time.perf_counter()
    if isOnly == 1:
        tempCount = da-xiao+1
        if number > tempCount:
            print("按唯一，数目不能少于da-xiao")
            pass
        else:
            while i < number:
                rand = random.randint(xiao, da)
                appear = only.count(rand)  # 元素出现次数
                if appear == 1:
                    i = i
                    j += 1
                else:
                    only.append(rand)
                    i += 1 
    elif isOnly == 0:
        while i < number:
            rand = random.randint(xiao, da)
            only.append(rand)
            i += 1
    else:
        print("outputError")
    
    print("\n随机名单如下：")
    print("-"*30)
    print("", end="\n")
    for i in range(len(only)):
        print("第%d位，随机生成数是：%d" % (i+1, only[i]))
    print("\n")
    print("-"*30)
    print("\n多余重复次数：%d"%j,end="\n")
    eTime = time.perf_counter()
    print("此次随机花费您Running time：%0.3f Seconds"%(eTime-sTime))
except Exception as result:
    print("error:", result)
