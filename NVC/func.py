import time
from selenium.webdriver.common.by import By


def wait(t):
    time.sleep(t)


def get_webpage(webdriver):
    webdriver.get("https://nvc.parim.co/")
    wait(2)


def logout(webdriver):
    pass


def get_email_password(webdriver):
    email = webdriver.find_element(By.ID, "LoginForm_email")
    email.send_keys(Email)
    password = webdriver.find_element(By.ID, "LoginForm_password")
    password.send_keys(Password)
    login = webdriver.find_element(By.ID, "login-btn")
    login.click()
    wait(5)
    logout(webdriver)


def clock_in(web_driver):
    btn = web_driver.find_element(By.CLASS_NAME, "shift-clock-in")
    btn.click()
    wait(10)
    print("Clocked IN")
    pass


def clock_out(web_driver):
    btn = web_driver.find_element(By.CLASS_NAME, "shift-clock-out")
    btn.click()
    wait(10)
    print("Clocked out")
    pass
