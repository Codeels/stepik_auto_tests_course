from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *
from math import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    book_button = browser.find_element(By.ID,"book")
    if WebDriverWait(browser,15).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100")):
        book_button.click()
    x = browser.find_element(By.ID,"input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(y)
    submit_button = browser.find_element(By.ID,"solve")
    submit_button.click()

finally:
    sleep(10)