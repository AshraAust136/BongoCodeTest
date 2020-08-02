import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")

driver.get("https://bongobd.com/")
driver.maximize_window()
driver.find_element_by_xpath("//INPUT[@placeholder='Search for videos']").send_keys("free videos",Keys.ENTER)

time.sleep(3)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]").click()



