from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys  # 한글 보여주는것
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")
    



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://flight.naver.com/flights/")


# 가는 날 클릭
driver.find_element_by_link_text("가는날 선택").click()
driver.find_elements_by_link_text("25")[0].click()

# 오는 날
driver.find_elements_by_link_text("29")[0].click()

# 제주도 클릭
driver.find_element_by_class_name("bg_gradient").click()

# 항공권 검색 클릭
driver.find_element_by_link_text("항공권 검색").click()

#time.sleep(10)  # 항공권 이 element가 출력이안되서 10초 sleep

try:
    elem = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
except:
    print("실패했어요")


# 첫 번째 결과 출력
#elem = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
#print(elem.text)        # element 내에 있는 text 부분 출력

time.sleep(5)
driver.quit()