#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:44:53 2019

@author: junlis
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
import re

def display_date():
    flight = browser.find_elements_by_css_selector(".search_box.search_box_tag.search_box_light.Label_Flight")
    counter = 0
    for a in flight:
        counter+=1
        info = a.find_element_by_css_selector(".logo-item.flight_logo").find_element_by_css_selector(
            "span").find_element_by_css_selector("span").find_element_by_css_selector("strong").text
        num = a.find_element_by_css_selector(".logo-item.flight_logo").find_element_by_css_selector(
            "span").find_element_by_css_selector("span").find_element_by_css_selector("span").text
        time1 = a.find_element_by_css_selector(".inb.right").find_element_by_css_selector(
            ".time_box").find_element_by_css_selector("strong").text
        place1 = a.find_element_by_css_selector(".inb.right").find_element_by_css_selector(".airport").text
        time2 = a.find_element_by_css_selector(".inb.left").find_element_by_css_selector(
            ".time_box").find_element_by_css_selector("strong").text
        place2 = a.find_element_by_css_selector(".inb.left").find_element_by_css_selector(".airport").text
        price = a.find_element_by_css_selector(".base_price02").text
        print(info, num, ":   ", time1, place1, "------", time2, place2, " 价格：", price)
        if counter == 5:
            break

def track(price, low, date, update):

    if low <= int(price):
        return low, update
    else:
        low = int(price)
        return low, date





browser = webdriver.Chrome()

browser.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
time.sleep(5)
browser.find_element_by_xpath('//*[@id="float_100_close"]').click()
browser.find_element_by_xpath('//*[@id="oversera_mask"]').click()
browser.find_element_by_xpath('//*[@id="searchBoxUl"]/li[2]/b').click()


#双击选择出发地
depart = browser.find_element_by_xpath('//*[@id="FD_StartCity"]')
ActionChains(browser).double_click(depart).perform()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="FD_StartCity"]').send_keys("南宁")

#出发日期
departDate = browser.find_element_by_xpath('//*[@id="FD_StartDate"]')
ActionChains(browser).double_click(departDate).perform()

browser.find_element_by_xpath('//*[@id="FD_StartDate"]').send_keys("2019-07-07")

#目的地选择
dest = browser.find_element_by_xpath('//*[@id="FD_DestCity"]')
ActionChains(browser).double_click(dest).perform()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="FD_DestCity"]').send_keys("杭州")
time.sleep(1)

#提交搜索
browser.find_element_by_xpath('//*[@id="FD_StartSearch"]').click()

dict = {}
low = 99999
update = ""
for i in range(5):
    date = browser.find_element_by_css_selector(".li.current").find_element_by_css_selector(".calendar_date").text
    base_price = browser.find_element_by_css_selector(".li.current").find_element_by_css_selector(".base_price02").text
    price = re.sub("¥", "", base_price)
    low, update = track(price, low, date, update)
    list = []
    list.append(price)
    print(date, "¥", price)

    display_date()
    time.sleep(3)

    block = browser.find_elements_by_css_selector(".slick-slide.slick-active")



    counter = 0
    for a in block:
        counter += 1
        test = a.find_element_by_css_selector(".li ").find_element_by_css_selector(".calendar_date").text
        if counter == 0:
           a.find_element_by_css_selector(".li ").click()
           break
        if test == date:
           counter = -1

    time.sleep(3)




browser.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')

browser.find_element_by_xpath('//*[@id="searchBoxUl"]/li[2]/b').click()

#双击选择出发地
depart = browser.find_element_by_xpath('//*[@id="FD_StartCity"]')
ActionChains(browser).double_click(depart).perform()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="FD_StartCity"]').send_keys("南宁")

#出发日期
departDate = browser.find_element_by_xpath('//*[@id="FD_StartDate"]')
ActionChains(browser).double_click(departDate).perform()
browser.find_element_by_xpath('//*[@id="FD_StartDate"]').clear()
new = "2019-"+re.sub("[周一,周二,周三,周四,周五,周六,周日]", "", update).rstrip()
browser.find_element_by_xpath('//*[@id="FD_StartDate"]').send_keys(new)

#目的地选择
dest = browser.find_element_by_xpath('//*[@id="FD_DestCity"]')
ActionChains(browser).double_click(dest).perform()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="FD_DestCity"]').send_keys("杭州")
time.sleep(1)

#提交搜索
browser.find_element_by_xpath('//*[@id="FD_StartSearch"]').click()

time.sleep(2)
browser.find_element_by_xpath('//*[@id="base_bd"]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[8]/button').click()
time.sleep(2)
new_col = browser.find_elements_by_css_selector(".search_table_inner_bar.search_table_inner.search-table-inner")
time.sleep(2)

new_col[0].find_element_by_css_selector(".btn_book").click()

"""
for a in new_col:
    a.find_element_by_css_selector(".btn_book").click()
    time.sleep(2)
    break
"""
time.sleep(2)
new_row = browser.find_elements_by_css_selector(".sale-item")
time.sleep(2)

try:
    new_row[0].find_element_by_css_selector(".btn_book").click()
    time.sleep(2)
except:
    print()
finally:
    browser.find_element_by_xpath('//*[@id="btn_nologin"]').click()

time.sleep(2)
name = browser.find_element_by_xpath('//*[@id="p_name_0"]')
ActionChains(browser).double_click(name).perform()
browser.find_element_by_xpath('//*[@id="p_name_0"]').send_keys("某某人")
time.sleep(1)
id = browser.find_element_by_xpath('//*[@id="p_card_no_0"]')
ActionChains(browser).double_click(id).perform()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="p_card_no_0"]').send_keys("331021198811040421")
time.sleep(2)
phone = browser.find_element_by_xpath('//*[@id="I_contact_phone"]')
ActionChains(browser).double_click(phone).perform()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="I_contact_phone"]').send_keys("15734768099")
time.sleep(1)

browser.find_element_by_xpath('//*[@id="J_saveOrder"]').click()
time.sleep(3)

dragger = browser.find_element_by_xpath('//*[@id="J_slider_verification"]/div[1]/div[2]')

ActionChains(browser).click_and_hold(dragger).perform()  # 鼠标左键按下不放

for index in range(200):
    try:
        ActionChains(browser).move_by_offset(10, 0).perform()  # 平行移动鼠标
    except UnexpectedAlertPresentException:
        break
    ActionChains(browser).reset_actions()
 