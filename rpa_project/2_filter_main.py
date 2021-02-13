from imap_tools import MailBox
from account import *
import sys  # 한글 보여주는것
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

applicant_list = []  # 지원자 리스트

with MailBox("imap.gmail.com", 993).login(
    EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX"
) as mailbox:
    index = 1  # 순번
    for msg in mailbox.fetch("(SENTSINCE 19-Jan-2021)"):  # 2021년 1월 19일 이후로 온 메일 조회
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")  # strip() 줄바꿈 없앰
            print("순번 : {} 닉네임: {} 전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

# for applicant in applicant_list:
# print(applicant)
