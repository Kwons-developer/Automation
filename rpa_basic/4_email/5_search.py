from imap_tools import MailBox
from account import *
import sys  # 한글 보여주는것
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

#mailbox = MailBox("imap.gmail.com", 993)
#mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# with 사용시 따로 logout 할 필요 없음
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    #for msg in mailbox.fetch(limit=5, reverse=True):
        #print("[{}] {}".format(msg.from_, msg.subject))

    # 읽지 않은 메일 가져오기
    #for msg in mailbox.fetch('(UNSEEN)'):       
        #print("[{}] {}".format(msg.from_, msg.subject))
    
    # 특정인이 보낸 메일 가져오기
    #for msg in mailbox.fetch('(FROM anstjdrnjs3@gmail.com)', limit =3, reverse=True):     
        #print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자 포함하는 메일(제목, 본문)
    #for msg in mailbox.fetch('(Text "test mail")'):         
        #print("[{}] {}".format(msg.from_, msg.subject))
    
    # 어떤 글자를 포함하는 메일 (제목만)
    #for msg in mailbox.fetch('(SUBJECT "text mail")'):      
        #print("[{}] {}".format(msg.from_, msg.subject))

    # 조건을 통해 한글을 가려내는 방법 (제목만)
    #for msg in mailbox.fetch(limit=5, reverse=True):
        #if "테스트" in msg.subject:
            #print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 이후의 메일 가져오기
    #for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', reverse=True, limit=5):     
        #print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜에 온 메일 받는 2번째 방법
    #for msg in mailbox.fetch('(ON 07-Nov-2020)', reverse=True, limit=5): 
        #print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건 모두 만족하는 메일  (and 조건)
    #for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "test mail")', reverse=True, limit=5):
        #print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건 중 하나라도 만족하는 메일   (or 조건)
    for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "test mail")', reverse=True, limit=5):
        print("[{}] {}".format(msg.from_, msg.subject))

        