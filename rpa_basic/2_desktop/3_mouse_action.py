import pyautogui

""" pyautogui.sleep(3)      # 3초 대기 3초 대기동안 마우스 이동해놓기 위해
print(pyautogui.position())
 """
#pyautogui.click(1025, 23, duration=1)
#pyautogui.mouseDown()
#pyautogui.mouseUp()
# 마우스 다운 + 마우스 업 = 클릭, 좌표없으면 현재위치에 실행


#pyautogui.doubleClick()
#pyautogui.click(clicks=500)     # 500번 클릭 2 하면 더블클릭 이랑 똒같음

#pyautogui.rightClick()      # 마우스 우클릭
#pyautogui.middleClick() # 마우스 휠 클릭
#pyautogui.drag()        # 현재 위치 기준으로 x,y 좌표로 드래그 동작이 너무 빨라서 drag 안될때 잇음 duration 값 지정
#pyautogui.dragTo()      # 절대 좌표 기준으로 좌표 위치로 드래그 이동


pyautogui.scroll(300)       #양수 이면 위 방향으로 300만큼 스크롤
# -300 은 알 방향으로 300만큼 스크롤



