from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time

# 네이버로 들어감
driver = webdriver.Chrome()
url = "https://naver.com"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element_by_css_selector(".link_login").click()
time.sleep(1)
# driver.find_element_by_css_selector("#id").click()
# action.send_keys("anstjdrnjs3").perform()

# id 와 pw 입력할 곳 찾음
ID = driver.find_element_by_css_selector("#id")
PW = driver.find_element_by_css_selector("#pw")
time.sleep(1)
# action.send_keys("flaks2357!").perform()

# id 입력
ID.click()
pyperclip.copy("anstjdrnjs3")
ID.send_keys(Keys.CONTROL, "v")
time.sleep(1)

# pw 입력
PW.click()
pyperclip.copy("flaks2357!")
PW.send_keys(Keys.CONTROL, "v")

driver.find_element_by_css_selector(".btn_global").click()