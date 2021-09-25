from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()
#driver.maximize_window()
driver.get('http://159.89.6.247:5000/login')
driver.find_element_by_name("password").send_keys(os.environ['LOGINPASS'])
driver.find_element_by_name("username").send_keys("John")
#driver.find_element_by_name("password").send_keys("12345")
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
#driver.find_element_by_class_name("mt-5") == "Hi, John!"
if(driver.find_element_by_xpath("//button[@class='btn btn-secondary']").is_displayed()):
    #print("Login testing Success!")
    os.system('echo Login testing Success')
else:
    #print("Login failed!")
    os.system('echo Login testing Failed')
driver.close()

