import pyautogui, pyperclip
import time
import sys  # 한글 보여주는것
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")


pyautogui.hotkey("win", "r")
pyautogui.sleep(1)
pyautogui.write("mspaint", interval = 0.25)
pyautogui.sleep(1)
pyautogui.hotkey("enter")

pyautogui.sleep(2)

w = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]

pyautogui.sleep(1)

w.maximize()

def paint_text(img_file, timeout = 30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file, confidence = 0.7)
        end = time.time()
        if end - start > timeout:
            break
    return target

def clickText(img_file, timeout = 30):
    target = paint_text(img_file, timeout)
    if target:
        pyautogui.click(target, duration=3)
    else:
        print("이미지를 찾지 못했습니다")
        sys.exit()


clickText("paintText.png", 10)

pyautogui.sleep(2)

text = pyautogui.locateOnScreen("text.png", region=(248, 330, 610 - 248, 631 - 330))
pyautogui.click(text)
# pyautogui.click(200, 200) 하는 방법도 있음


""" 248,330 255,255,255 #FFFFFF
610,631 255,255,255 #FFFFFF """

pyperclip.copy("안녕하세요")
pyautogui.hotkey("ctrl", "v")

pyautogui.sleep(5)

clickText("paintExit.png", 10)
# window.close() 방법

pyautogui.sleep(1)

pyautogui.press("n")

# 특정 이미지를 기준으로 상대좌표로 다른 이미지 사용하기
# 이미지 = pyautogui.locateOnScreen("브러시이미지.png")
#pyautogui.click(이미지.left-200, 이미지.top+200)