from email.mime.multipart import MIMEMultipart 

from email.mime.text import MIMEText 

from email.mime.image import MIMEImage

from pathlib import Path

content = MIMEMultipart()
content['From'] = 'test@gmail.com@gmail.com'
content['To'] = 'test2@gmail.com'
content['Subject'] = '測試gmail_by_lordarcher'

# 純文字內容
content.attach(MIMEText('lord你好,\n' + 'gmail發送測試成功\n' + '{:20}by Frank'.format('')))

# 圖片
content.attach(MIMEImage(Path('多拉.jpg').read_bytes()))

# 連線到server
import smtplib

server = smtplib.SMTP_SSL(host = 'smtp.gmail.com',port = 465) # gmail server
server.login('test@gmail.com', '123456789') # 發送端帳戶(帳,密)
server.send_message(content)
server.close()
print('Complete!')