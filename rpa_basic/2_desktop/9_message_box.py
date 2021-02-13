import pyautogui
import sys  # 한글 보여주는것
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

#pyautogui.countdown(3)      # 시스템 3초 기다리게 가능
#print("자동화 시작")

#pyautogui.alert("자동화 수행에 실패하였습니다.", "경고")        # 확인 버튼만 있는 팝업
#pyautogui.confirm("계속 진행하시겠습니까?", "확인")
#result = pyautogui.confirm("계속 진행하시겠습니까?", "확인")
#print(result)

#result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")    # 사용자 입력
#print(result)       # 취소, 아님 x 누르면 None 반환
result = pyautogui.password("암호를 입력하세요")        # 암호입력
print(result)