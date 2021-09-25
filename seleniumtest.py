from selenium import webdriver

import time
import os

driver = webdriver.Chrome()
#driver.maximize_window()
driver.get('http://159.89.6.247:5000/login')
driver.find_element_by_name("password").send_keys(os.environ['LOGINPASS'])
driver.find_element_by_name("password").send_keys("12345")
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
#driver.find_element_by_class_name("mt-5") == "Hi, John!"
if(driver.find_element_by_class_name("mt-5").is_displayed()):
    print("Login testing Success!")
else:
    print("Login failed!")
driver.close()

