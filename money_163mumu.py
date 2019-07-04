# mumu模拟器专版

# 请调整模拟器分辨率：长1920 宽1080

import os
import time

count=0
def get():
    print("正在刷新...")
    os.system('adb shell input tap 105 1890')
    time.sleep(0.5)
    print("刷新成功")

    print("点开第",count+1,"条新闻")
    os.system('adb shell input tap 300 600')
    time.sleep(1)

    for i in range(1, 30):
        print("阅读中，剩余", 30 - i, "秒")
        os.system('adb shell input swipe 560 1000 550 426')

    print("返回主页面")
    os.system('adb shell input tap 51 130')

    # 时段奖励（45分钟1次）
    if((count%90)==0):
        os.system('adb shell input tap 966 132')
        time.sleep(0.5)
        os.system('adb shell input tap 909 518')


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