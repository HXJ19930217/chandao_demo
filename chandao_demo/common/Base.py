# conding = 'utf-8'
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class Base():
    def __init__(self,driver:webdriver.Firefox):
        self.driver=driver
        self.timeout = 10

    def find_element(self,*loc):
         ele=self.driver.find_element(*loc)
         return ele

    def input_text(self,loc,txt):
        self.find_element(*loc).send_keys(txt)

    def click(self,loc):
        self.find_element(*loc).click()

    def clear(self,loc):
        self.driver.find_element(*loc).clear()

    def select_index(self,loc,index):
        Select(self.driver.find_element(*loc)).select_by_index(index)   # 根据索引选择

    def select_value(self, loc,  value):
        Select(self.driver.find_element(*loc)).select_by_value(value)  # 根据value值选择





    def sleep_time(self,time):
        sleep(time)








