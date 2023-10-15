from selenium import webdriver
from selenium.webdriver.common.by import By
from NVC import func as f
import time

driver = webdriver.Chrome()


def time_com(web_driver):
    if (time.strftime('%H:%M') < '17:55') & (time.strftime('%H:%M') == '17:55'):
        if web_driver.find_element(By.CLASS_NAME, "shift-clock-in"):
            f.clock_in(web_driver)

    elif(time.strftime('%H:%M') == '06:25') & (time.strftime('%H:%M') < '06:32'):
        if web_driver.find_element(By.CLASS_NAME, "shift-clock-out"):
            f.clock_out(web_driver)
            print("Clocked IN")
    else:
        raise Exception('Sorry, none completed')
    time.sleep(2)


def main():
    f.get_webpage(driver)
    f.get_email_password(driver)
    time_com(driver)
