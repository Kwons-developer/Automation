import pyautogui
#pyautogui.mouseInfo()
# 마우스 자동 동작 취소하고 싶으면 구석 귀퉁이로 마우스 보내면 됨
#pyautogui.FAILSAFE = False # 마우스 귀퉁이로 보내도 취소 안되게 하는것

pyautogui.PAUSE=1 # 모든 동작에 1초씩 sleep 적용


for i in range(10):
    pyautogui.move(100, 100, duration = 2)
