from selenium import webdriver
import time
import sys  # 한글 보여주는것
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.w3schools.com/tags/att_input_type_radio.asp")
curr_handle = driver.current_window_handle
print(curr_handle)      # 현재 윈도우 핸들 정보 가져옴


driver.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = driver.window_handles # 모든 핸들 정보 가져옴
for handle in handles:
    print(handle)
    driver.switch_to.window(handle) # 각 핸들로 이동
    print(driver.title)     #출력하면 현재 핸들 (브라우저) 의 제목 표시
    print()

# 새로 이동된 브라우저에서 뭔가 자동화 작업 수행...
# 열린 브라우저 종료
print("현재 핸들 닫기")
driver.close()


# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
driver.switch_to.window(curr_handle)


print(driver.title)


# 브라우저 컨트롤 가능한지 확인 
time.sleep(5)
driver.get("http://daum.net")



time.sleep(5)
driver.quit()