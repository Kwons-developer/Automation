import pyautogui
import sys  # 한글 보여주는것
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")


#fw = pyautogui.getActiveWindow()    # 현재 활성화된 창 정보 가져오는것임
#print(fw.title)     # 창의 제목 정보 가져옴
#print(fw.size)      # 창의 크기 정보 가져옴
#print(fw.left, fw.top, fw.right, fw.bottom)  # 창의 좌표 정보
#pyautogui.click(fw.left + 100, fw.top + 20)     # 떠 있는 창의 좌표에 클릭

#for w in pyautogui.getAllWindows():
#   print(w)    # 모든 창 가져오기
    
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:     #현재 활성화 되지 않았다면
    w.activate()        # 활성화 (맨 앞으로 가져옴)


if w.isMaximized == False:
    w.maximize()        # 최대 화면
#if w. isMinimized == False:
#    w.minimize()        # 최소 화면

w.restore()         # 화면 크기 원상복귀

w.close()       # 윈도우 닫기