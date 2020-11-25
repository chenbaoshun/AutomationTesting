#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : test_douban.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-23

import pytest
import time
from selenium import webdriver

class Test_douban():
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_open_douban(self):
        # 打开豆瓣首页
        self.driver.get("https://www.douban.com/")
        self.driver.implicitly_wait(10)

    def test_open_mov(self):
        # 打开电影首页
        self.driver.find_element_by_css_selector('.lnk-movie').click()

        handles = self.driver.window_handles
        print(f'当前的页面句柄：{handles}')
        self.driver.switch_to.window(handles[-1])

    def test_into_hot_mov(self):
        # 进入一个项目，例如“热门电影”
        self.driver.find_element_by_xpath('//*[text()="最近热门电影"]/following-sibling::a[text()="更多»"]').click()

    def test_loop_info(self):
        # 循环检查这个页面里，链接的信息和详细页面的内容
        more = self.driver.find_element_by_xpath('//*[text()="加载更多"]')

        # '//h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a'#找到所有的电影连接
        mov_list = self.driver.find_elements_by_xpath('//h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a')
        print(f'当前的电影清单：{mov_list}')

        # //h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a/div/img
        for i in range(1, len(mov_list)):
            time.sleep(2)
            mov_name = self.driver.find_element_by_xpath(
                f'//h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a[{i}]/div/img').get_attribute('alt')
            print(f'获取到的电影名字是：{mov_name}')

            # //h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a[1]/p/strong
            mov_score = self.driver.find_element_by_xpath(
                f'//h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a[{i}]/p/strong').get_attribute('text')
            print(f'获取到的电影评分是：{mov_score}')
            time.sleep(5)
            # mov_list[i-1].click()   # 打开详细页面
            self.driver.execute_script("arguments[0].click();", mov_list[i - 1])

            handles = self.driver.window_handles
            print(f'当前的页面句柄:{handles}')
            time.sleep(5)
            self.driver.switch_to.window(handles[-1])  # 切换句柄到详细页面
            time.sleep(2)

            # //*[text()="除暴"]
            # info_name = driver.find_element_by_xpath('//*[text()="除暴"]')
            info_name = self.driver.find_element_by_xpath('//*[@id="wrapper"]//h1').text
            assert mov_name in info_name
            self.driver.close()
            time.sleep(5)
            self.driver.switch_to.window(handles[-2])  # 手动把操作的窗口切换到上一个

if __name__ == '__main__':
    pytest.main()
