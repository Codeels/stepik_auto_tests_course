from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    robot_checkbox = browser.find_element(By.CSS_SELECTOR,"#robotCheckbox")
    people_radio = browser.find_element(By.CSS_SELECTOR,"#peopleRule")
    robot_radio = browser.find_element(By.CSS_SELECTOR,"#robotsRule")

    #проверка чекбокса на исходное состояние (не нажат)
    robot_checkbox_checked = robot_checkbox.get_attribute("checked")
    print('robot_checkbox_checked =', robot_checkbox_checked)
    assert robot_checkbox_checked != "true", "its checked by default"

    #проверка радиобатона с человеком на нажатость
    people_radio_checked = people_radio.get_attribute("checked")
    print('people_radio_checked =', people_radio_checked)
    assert people_radio_checked != "true", "its checked by default"

    #проверка радиобатона с роботом на нажатость
    robot_radio_checked = robot_radio.get_attribute("checked")
    print('robot_radio_checked =', robot_radio_checked)
    assert robot_radio_checked != "true", "its checked by default"

finally:
    time.sleep(5)