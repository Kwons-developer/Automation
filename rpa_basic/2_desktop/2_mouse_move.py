import pyautogui


# 마우스 이동  ( 절대 좌표로 마우스 이동)
# 왼쪽 상단이 (0,0)임
#pyautogui.moveTo(200, 100) # 지정한 위치로 마우스 이동
#pyautogui.moveTo(100, 200, duration=5)   # 0.25 초 동안 100, 200 위치로 이동

# 상대 좌표로 마우스 이동 (현재 커서가 있는 위치로부터)
pyautogui.moveTo(100, 100, duration=3)
print(pyautogui.position())
pyautogui.move(100, 100, duration=2)
print(pyautogui.position())
pyautogui.move(100, 100, duration=2)
print(pyautogui.position())


p = pyautogui.position()
print(p[0], p[1]) # x, y 좌표
print(p.x, p.y)         # x,y 좌표

