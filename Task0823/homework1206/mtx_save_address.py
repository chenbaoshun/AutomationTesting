#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : mtx_save_address.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-03 21:46

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

saveaddress_url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/useraddress/index.html'
driver = webdriver.Chrome()

driver.get("http://121.42.15.146:9090/mtx/")
sleep(1)
driver.add_cookie({'name':'PHPSESSID', 'value':'0lorcqq7trrme8ncabauvhs6k7'})
sleep(2)
driver.refresh()

driver.get(saveaddress_url)

add_address = driver.find_element_by_xpath("//button[@type='button']/following::button[4]").click()

# WebDriverWait(driver, 20, 0.5).until(EC.frame_to_be_available_and_switch_to_it(lambda e:e.find_element_by_xpath("//iframe/following::iframe[2]")))
driver.switch_to.frame(driver.find_element_by_xpath("//iframe/following::iframe[2]"))
sleep(3)
name_input = driver.find_element_by_xpath("//input[@name='name']").send_keys("chin")
phone_input = driver.find_element_by_name("tel").send_keys("13029928834")
sleep(1)
# province_select = Select(driver.find_element_by_xpath("//label[@class='block']/following-sibling::div[1]")).select_by_index(3)
province_element = driver.find_element_by_xpath("//div[contains(@class,'chosen-container')][1]").click()
sleep(3)
province_select = Select(driver.find_element_by_xpath("//*[@name='province']")).select_by_value("2")
# province_select.find_element_by_xpath("//li[@data-option-array-index='1']").click()
# //*[@name='province']

sleep(2)
city_select = Select(driver.find_element_by_xpath("//*[@name='city']")).select_by_value("57")
sleep(2)
county_select = Select(driver.find_element_by_xpath("//*[@name='county']")).select_by_index(3)
sleep(2)
address_input = driver.find_element_by_name("address").send_keys("武侯大道369")
alias_input = driver.find_element_by_name("alias").send_keys("默认地址")
is_default = driver.find_element_by_xpath("//*[text()='是否默认']/following-sibling::div").click()
sleep(3)

save_button = driver.find_element_by_xpath("//button[text()='保存']").click()
sleep(3)