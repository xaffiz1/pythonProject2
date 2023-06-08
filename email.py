import smtplib

password_email = 'jxnbqsxizlfvuncv'
sender = "xaffiz92@gmail.com"
server = "smtp.gmail.com"
port = 465
reciever ="absaitovdev@gmail.com"

message = f"""
Github_link : https://github.com/xaffiz1/pythonProject2.git
Sender : Abdulxafiz"""
with smtplib.SMTP_SSL(server, port) as server:
    server.login(sender, password_email)
    server.sendmail(sender, reciever, message)