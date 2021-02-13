import pyautogui
# 스크린 샷 찍기

#img = pyautogui.screenshot()        # 스크린샷 찍음
#img.save("screenshot.png") # 파일로 저장 저장 될때는 지금 코드 폴더에 저장 됨


#pyautogui.mouseInfo()

#991,23 33,164,241 #21A4F1

pixel = pyautogui.pixel(991, 23)
print(pixel)

#pyautogui.pixelMatchesColor(28,18,(34, 167, 242))       # 좌표 와 rgb 값 일치하는지 true, false 값 리턴
