'''

by Daniel Sun
'''
import time
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys



def main():
    conf = configHandler()

    options = Options()
    options.add_argument("start-maximized") # maximized window size
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    service = Service("./bin/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(conf.get('url', 'https://www.google.com'))

    driver.find_element(By.XPATH, '/html/body/main/a').click()  # click booking

    account = driver.find_element(By.XPATH, '//*[@id="user_email"]')  # user name
    account.clear()
    account.send_keys(conf['user'])
    password = driver.find_element(By.XPATH, '//*[@id="user_password"]')  # password
    password.clear()
    password.send_keys(conf['password'])
    driver.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click()  # login

    driver.find_element(By.XPATH, '/html/body/main/a[24]').click()  # choose route

    driver.find_element(By.XPATH, '/html/body/main/a').click()  # click booking again


    time.sleep(3)
    driver.close()
    print("bye bye~")


def login():
    pass

def configHandler():
    conf = {}
    try:
        config = configparser.ConfigParser()
        config.read('./conf/config.txt')
        conf['url'] = config.get('default', 'URL')
        conf['user'] = config.get('default', 'User')
        conf['password'] = config.get('default', 'Password')
        print(f'config loading complete: {conf}')
    except Exception as e:
        print(e)
    return conf


if __name__ == "__main__":
    main()