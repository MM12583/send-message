from twilio.rest import Client # 用戶端

account_sid = 'AC43885269wed0a01670aaa6564da77e77'

auth_token = '2896wg937ji03832eca580a0af58536a'

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='簡訊成功寄出,恭喜！',
         from_='+18521064296',
         to='+8882579453684'
     )

print(message.sid)