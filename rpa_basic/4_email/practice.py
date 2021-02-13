""" to_list = ["anstjdrnjs3@gmail.com", "anstjdrnjs3@naver.com"]
msg = ", ".join(to_list)    # "" 사이에있는 것으로 구분
print(msg)
 """
""" 
import time
print(time.strftime('%d-%a-%Y'))    # 현재 날짜를 일-요일-연도 출력

import datetime
dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")
print(type(dt))
print(dt.strftime('%d-%a-%Y')) """



""" 
import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "제목"
msg["From"] = "발신자"
msg["To"] = "수신자"

to_list = ["이메일1", "이메일2"]
msg["To"] = ", ".join(to_list)
msg.set_content("본문")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    
    smtp.send_message(msg) """

""" 
import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "anstjdrnjs3@gmail.com"
msg.set_content("다운로드")

with open("button.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)


with open("~~.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("quiz.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg) """


from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    print("날짜", msg.date)
    print("본문", msg.text)
    print("HTML 메시지", msg.html)
    print("=" * 100)
    
    for att in msg.attachments:
        print("첨부파일 이름", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)
        
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("첨부파일 {} 다운로드 완료".format(att.filename))

    mailbox.logout