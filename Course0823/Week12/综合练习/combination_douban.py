#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : combination_douban.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-22 13:47
# @Site    : 
# @version : V1.0

# 目的：综合练习selenium操作
# 需求：
# 进入豆瓣电影的某一个栏目，检查电影详细页面的跳转正常
# 分解操作：
# 1.打开豆瓣首页
#     get
# 2.打开电影页面
#     click电影按钮
#     由于会打开新标签，所以切换标签
# 3.进入一个项目，例如“热门电影”
# 4.循环检查这个页面里，链接的信息和详细页面的内容
#     获取连接的“电影名称”属性
#     点击连接，进入详细页面
#     对详细页面中电影名称的属性进行检查
#     退回到链接页面

from time import sleep
from selenium import webdriver

# 初始化浏览器驱动实例
driver = webdriver.Chrome()

# 打开豆瓣首页
driver.get("https://www.douban.com/")
driver.implicitly_wait(10)

# 打开电影首页
driver.find_element_by_css_selector('.lnk-movie').click()

handles = driver.window_handles
print(f'当前的页面句柄：{handles}')
driver.switch_to.window(handles[-1])

# 进入一个项目，例如“热门电影”
driver.find_element_by_xpath('//*[text()="最近热门电影"]/following-sibling::a[text()="更多»"]').click()

# 循环检查这个页面里，链接的信息和详细页面的内容
more = driver.find_element_by_xpath('//*[text()="加载更多"]')

# '//h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a'#找到所有的电影连接
mov_list = driver.find_elements_by_xpath('//h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a')
print(f'当前的电影清单：{mov_list}')

# //h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a/div/img
for i in range(1, len(mov_list)):
    sleep(2)
    mov_name = driver.find_element_by_xpath(f'//h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a[{i}]/div/img').get_attribute('alt')
    print(f'获取到的电影名字是：{mov_name}')

    # //h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a[1]/p/strong
    mov_score = driver.find_element_by_xpath(f'//h1[text()="选电影"]/following::div[@class="list-wp"]/child::div/a[{i}]/p/strong').get_attribute('text')
    print(f'获取到的电影评分是：{mov_score}')
    sleep(5)
    # mov_list[i-1].click()   # 打开详细页面
    driver.execute_script("arguments[0].click();", mov_list[i-1])

    handles = driver.window_handles
    print(f'当前的页面句柄:{handles}')
    sleep(5)
    driver.switch_to.window(handles[-1])  # 切换句柄到详细页面
    sleep(2)

    # //*[text()="除暴"]
    # info_name = driver.find_element_by_xpath('//*[text()="除暴"]')
    info_name = driver.find_element_by_xpath('//*[@id="wrapper"]//h1').text
    assert mov_name in info_name
    driver.close()
    sleep(5)
    driver.switch_to.window(handles[-2])    # 手动把操作的窗口切换到上一个