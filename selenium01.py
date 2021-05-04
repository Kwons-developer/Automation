from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "http://naver.com"
driver.get(url)

driver.find_element_by_css_selector(".input_text").send_keys("대구대학교")
driver.find_element_by_css_selector(".input_text").send_keys(Keys.ENTER)

driver.find_element_by_css_selector(".sub_wrap").click()