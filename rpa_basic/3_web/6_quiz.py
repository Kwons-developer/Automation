from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys  # 한글 보여주는것
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")
import time

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/")
driver.maximize_window()

# LEARN HTML 클릭
driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/a[1]').click()

# HOW TO 클릭
driver.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]').click()

# CONTACT FORM 클릭
driver.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()
#이런식으로 a 태그 안에 text로도 접근 가능
#driver.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]')
#contains 는 contact 문자 포함하는것에 접근
#driver.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]')

# first name 에 "나도" 작성
first_name = driver.find_element_by_xpath('//*[@id="fname"]')
first = "나도"
first_name.send_keys(first)

# Last name 에 "코딩" 작성
Last_name = driver.find_element_by_xpath('//*[@id="lname"]')
Last = "코딩"
Last_name.send_keys(Last)

# country canada  선택
driver.find_element_by_xpath('//*[@id="country"]/option[2]').click()
#country = "Canada"
#driver.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()


# subject 작성
subject_name = driver.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
subject = "퀴즈 완료하였습니다."
subject_name.send_keys(subject)

time.sleep(5)

# subject 버튼 클릭
driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()



time.sleep(5)
driver.quit()   # close 는 현재 탭만 닫음
