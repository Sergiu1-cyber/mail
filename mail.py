import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email = 'sergiu-manza@mail.ru'
passworld = 'WPmxRwWqtQiBaM2XhNYv'

msg = MIMEMultipart()
to_email = 'manzasergiu@gmail.com'
message = 'mesaj expediat cu ajutorul python'

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.mail.ru', 25)
server.starttls()
server.login(from_email, passworld)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()


