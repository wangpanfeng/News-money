# mumu模拟器专版

# 请调整模拟器分辨率：长1920 宽1080 dpi 320

import os
import time
import random

count=0
def get():
    print("正在刷新...")
    os.system('adb shell input tap 113 1877')
    time.sleep(2)
    print("刷新成功")

    print("点开第",count+1,"条新闻")
    os.system('adb shell input tap 300 600')
    time.sleep(2)
    maxtime = 20
    for i in range(1, maxtime):
        print("阅读中，剩余", maxtime - i, "秒")
        # os.system('adb shell input swipe 560 1000 550 426')
        # 随机，随机，随机！！！
        startX = random.randint(460, 660)
        startY = random.randint(900, 1100)
        endX = random.randint(450, 550)
        endY = random.randint(326, 526)
        os.system("adb shell input swipe " + str(startX) + ' ' + str(startY) + ' ' + str(endX) +  ' ' + str(endY))


    print("返回主页面")
    os.system('adb shell input tap 51 130')

    # 时段奖励（1小时1次）
    if ((count % 120) == 0):
        os.system('adb shell input tap 991 84')
        time.sleep(0.5)
        os.system('adb shell input tap 991 84')


print("无限循环 or 循环n次？[1|2]")
a = input("请输入1或2：")


if a == '1':
    print("----无限循环模式启动----")
    while 1:
        get()
        count += 1
elif a == '2':
    n = input("请输入遍数：")
    print("----循环",n,"遍----")
    for count in range(0, int(n)):
        get()