import os
import time


print("正在刷新...")
os.system('adb shell input swipe 550 426 560 1700')
print("刷新成功")

print("点开第一条新闻")
os.system('adb shell input tap 300 600')

for i in range(1,30):
    print("阅读中，剩余", 30-i,"秒")
    os.system('adb shell input swipe 560 1000 550 426')

print("返回主页面")
os.system('adb shell input tap 51 130')