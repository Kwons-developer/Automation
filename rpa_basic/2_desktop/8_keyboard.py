import pyautogui
import sys  # 한글 보여주는것
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")


w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

#pyautogui.write("12345")
#pyautogui.write("nadocoding", interval=0.25)       # 글 하나마다 1초씩 걸리게함
#pyautogui.write("나도코딩") # 는 한글은 안됨 오직 숫자, 영어만 가능

#pyautogui.write(["t","e","s","t","left","right","l","a","enter"], interval=0.25)


# 특수 문자
#pyautogui.keyDown("shift")
#pyautogui.press("4")    # press 는 눌렀다 빼는것
#pyautogui.keyUp("shift")

# 조합키 
#pyautogui.keyDown("ctrl")
#pyautogui.keyDown("a")
#pyautogui.keyUp("a")
#pyautogui.keyUp("ctrl")

# 간편한 조합키
#pyautogui.hotkey("ctrl", "alt", "shift", "a")
# ctrl 누르고 alt 누르고 shift 누르고 a 누르고 a 떼고 shift 떼고 alt 떼고 ctrl 떼고 순서임

#pyautogui.hotkey("ctrl","a")    # ctrll + a


# pip install pyperclip 다운

import pyperclip
pyperclip.copy("나도코딩")      # 나도코딩 클자 클립보드에 저장
pyautogui.hotkey("ctrl", "v")

# win : ctrl + alt + del 누르면 자동화 정지
