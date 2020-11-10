import email.message as emsg

msg = emsg.EmailMessage()
msg['From'] = 'ewfwefwefw@gmail.com'
msg['To'] = 'molkmokm@gmail.com'
msg['Subject'] = '測試gmail_by_hcy'

# 純文字內容
msg.set_content('lord你好,\n' + 'gmail發送測試成功\n' + 'Frank')

# 寄送多樣式內容 (html)
msg.add_alternative('<h3>優惠券</h3>滿千送百', subtype = 'html')

# 連線到server
import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # gmail server
server.login('hgfhghrh@gmail.com', '6ygnhjt') # 發送端帳戶(帳,密)
server.send_message(msg)
server.close()