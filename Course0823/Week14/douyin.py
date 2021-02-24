#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : douyin.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-10 23:01

# 0.手机上需要安装抖音APP
# 1.对driver进行实例化
# 2.滑动 和 获取文本操作
# 3.清场

# 1.编写启动项
from time import sleep
from appium import webdriver

caps = {}
caps['noReset'] = "true"#跳过重签名
caps["platformName"] = 'Android'
caps['deviceName'] = 'Phone'
#一般来说,在脚本的启动项中需要指定包名和界面名(启动)
caps['appPackage'] = 'com.ss.android.ugc.aweme'
caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'

# 2.初始化设备实例
driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)

# 编写动作
# =========
# 关于滑动:从屏幕中间向上滑动.考虑到手机分辨率可能变化,所以需要一个相对坐标滑动的方法
def swipe_test(x1=0.6,y1=0.75,x2=0.6,y2=0.1,duration=500):
    size = driver.get_window_size()#获取设备尺寸
    # print(size)
    x1 = x1 * size['width']
    x2 = x2 * size['width']
    y1 = y1 * size['height']
    y2 = y2 * size['height']
    driver.swipe(x1,y1,x2,y2,duration=duration)

for i in range(3):
    swipe_test()
    sleep(3)
    id = "com.ss.android.ugc.aweme:id/title"
    # xpath = "//androidx.viewpager.widget.ViewPager[@content-desc='视频']/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView"
    name = driver.find_element_by_id(id).get_attribute('text')
    id = "com.ss.android.ugc.aweme:id/a9_"
    info = driver.find_element_by_id(id).get_attribute('text')

    print(f'第{i+1}个视频')
    print(f'当前视频的作者是:{name}')
    print(f'视频简介是:{info}')

driver.quit()