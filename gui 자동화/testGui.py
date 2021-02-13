import pyautogui, time
import sys  # 한글 보여주는것
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")


w = pyautogui.getWindowsWithTitle("컴퓨터자격증")[0]
if w.isActive == False:
    w.activate()

""" obs = pyautogui.getWindowsWithTitle("OBS")[0]
end_record = pyautogui.locateOnScreen("녹화끝.png", region = (179, 226,539-179,570-226)) """
""" 179,226 0,0,0 #000000

539,570 0,0,0 #000000
 """

pyautogui.sleep(3)

# 이미지 찾기
def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file, confidence = 0.7)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target, duration = 0.15)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()
    

def multify(img_file):
    target = pyautogui.locateAllOnScreen(img_file, confidence = 0.7)
    if target:
        for i in target:
            pyautogui.click(i, duration = 0.25)
            for x in range(0, 3):
                obs = pyautogui.getWindowsWithTitle("OBS")[0]
                pyautogui.sleep(2)
                obs.activate()
                pyautogui.sleep(2)
                my_click("recordstart.png",10)
                pyautogui.sleep(2)
                obs.minimize()
                pyautogui.sleep(2)
                it = pyautogui.getWindowsWithTitle("아이티 버팀목")[0]
                pyautogui.sleep(1)
                it.maximize()
                pyautogui.sleep(2)
                class_max = pyautogui.locateOnScreen("수업화면최대화.png", region = (881,905,908-881,928-905),confidence = 0.7)     # 비디오 플랫폼 클릭 못하고 있음
                pyautogui.click(class_max)
                break

    else:
        print("이미지 찾기 실패")
        sys.exit()

multify("realtime.png")
""" 
881,905 46,46,46 #2E2E2E
908,928 77,77,77 #4D4D4D """