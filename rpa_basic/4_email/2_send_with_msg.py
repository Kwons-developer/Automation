import smtplib
from account import *
from email.message import EmailMessage

# 메일 한글로 보내려면 EmailMessage() 객체 이용해야함

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."   # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "anstjdrnjs3@gmail.com" # 받는사람

# 여러 명에게 메일 보낼 때
#msg["To"] = "anstjdrnjs3@gmail.com", "anstjdrnjs3@naver.com"
#to_list = ["anstjdrnjs3@gmail.com", "anstjdrnjs3@naver.com"]
#msg["To"] = ", ".join(to_list)

# 참조
#msg["Cc"] = "anstjdrnjs3@gmail.com"

#비밀 참조
#msg["Bcc"] = "anstjdrnjs3@gmail.com"


msg.set_content("테스트 본문입니다")    # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)