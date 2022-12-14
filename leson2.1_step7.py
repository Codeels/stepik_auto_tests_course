from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    valuex = browser.find_element(By.ID, "treasure")
    value = valuex.get_attribute("valuex")
    result = calc(value)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(result)
    robot_checkbox = browser.find_element(By.ID,"robotCheckbox")
    robot_checkbox.click()
    robot_radio = browser.find_element(By.CSS_SELECTOR,"#robotsRule")
    robot_radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)