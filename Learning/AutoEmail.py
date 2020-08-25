import smtplib
import sender

from email.utils import formataddr
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def Send_eamil(sender,password,content,receive):
    receives = receive
    msg = MIMEMultipart()

    msg["Subject"] = "雲涯筆尖文化"
    msg["From"] = sender
    if len(receives)>1:
        msg["To"] = ",".join(receives)
    else:
        msg["To"] = receives[0]

    part = MIMEText(content,_charset="UTF-8")
    msg.attach(part)
    try:
        smtp = smtplib.SMTP_SSL("smtp.126.com")
        smtp.login(sender,password)
        smtp.sendmail(sender,receives,msg.as_string())

        print("邮件发送成功")

    except smtplib.SMTPException as e:
        print("ERROR，发送失败")
    finally:
        smtp.quit()
sender,password = sender.sender()
content = "测试邮件发送功能"
recevice = ["dlpu_gulang@126.com"]
Send_eamil(sender,password,content,recevice)