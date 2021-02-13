import pyautogui
import time, sys

# 화면 내에서 이미지 를 찾아냄
# 윈도우키 + 쉬프트 + s 로 캡쳐
#file_menu = pyautogui.locateOnScreen("file_menu.png")
#print(file_menu)    # 파일 이미지의 좌표위치와 가로, 세로 폭 알려줌

#pyautogui.click(file_menu)

# 인자가 없거나 다른 스크린샷을 찾으라고하면 None 값 반환

#pyautogui.locateAllOnScreen("")     # 내가 지정한 이미지의 모든 정보 가져옴

#locateOnScreen 은 이미지 에서 처음 발견하는것을 다루고
#locateAllOnScreen 은 지정한 이미지랑 똑같은 모든것을 다룸



# 속도 개선
# 1. GrayScale
#file_menu = pyautogui.locateOnScreen("file_menu.png", grayscale=True)
#pyautogui.click(file_menu)

# 2. 범위 지정
#file_menu = pyautogui.locateOnScreen("file_menu.png", region=(967, 4, 1369 - 967, 35 - 4))
#pyautogui.click(file_menu)
""" 967,4
1369,35 """

# 3. 정확도 조정
#run_btn = pyautogui.locateOnScreen("start_menu.png", confidence=0.9)        # 90퍼센트 정확도
#pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리는것
""" file_menu_notepad = None

while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
    print("발견 실패")

pyautogui.click(file_menu_notepad) """


""" # 2. 일정 시간동안 기다리기 (TimeOut)
timeout = 10 # 10초 대기
start = time.time()      # 시작 시간 설정
file_menu_notepad = None

while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
    end = time.time()       # 종료 시간 설정

    if end - start > timeout:       # 지정한 10초 초과하면
        print("시간 종료")
        sys.exit()  

pyautogui.click(file_menu_notepad) """

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()


    
my_click("file_menu_notepad.png", 10)

