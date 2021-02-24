#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_douyin.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-09 23:43

# 0.手机上需要安装抖音APP
# 1.对driver进行实例化
# 2.滑动 和 获取文本操作
# 3.清场

# 1.编写启动项
from time import sleep
import pytest
from appium import webdriver

class Test_douyin():

    caps = {}
    caps['noReset'] = "true"  # 跳过重签名
    caps["platformName"] = 'Android'
    caps['deviceName'] = 'Phone'
    # 一般来说,在脚本的启动项中需要指定包名和界面名(启动)
    caps['appPackage'] = 'com.ss.android.ugc.aweme'
    caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'

    # 前置方法
    def setup_class(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.caps)

    # 清场方法
    def teardown_class(self):
        self.driver.quit()


    # 2.初始化设备实例
    # driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)

    # 编写动作
    # =========
    # 关于滑动:从屏幕中间向上滑动.考虑到手机分辨率可能变化,所以需要一个相对坐标滑动的方法
    def test_douyin_01(self):

        def image_swipe(x1=0.6,y1=0.75,x2=0.6,y2=0.1,duration=500):
            size = self.driver.get_window_size()#获取设备尺寸
            # print(size)
            x1 = x1 * size['width']
            x2 = x2 * size['width']
            y1 = y1 * size['height']
            y2 = y2 * size['height']
            self.driver.swipe(x1,y1,x2,y2,duration=duration)

        for i in range(3):
            image_swipe()
            sleep(3)
            id = "com.ss.android.ugc.aweme:id/title"
            name = self.driver.find_element_by_id(id).get_attribute('text')
            id = "com.ss.android.ugc.aweme:id/a9_"
            info = self.driver.find_element_by_id(id).get_attribute('text')

            print(f'第{i + 1}个视频')
            print(f'当前视频的作者是:{name}')
            print(f'视频简介是:{info}')

if __name__ == '__main__':
    pytest.main()