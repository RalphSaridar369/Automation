import smtplib

# insert here your email destinations

mail_to=['']

# insert here your message

message="This is just a test"

# insert the email of the person sending the mail

mail_Sent_From = 'insert your email here'
password = 'insert password here'

def send_from_Gmail():

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(mail_Sent_From,password)

    for email in mail_to:
        server.sendmail(mail_Sent_From,email,message)

    server.quit()

send_from_Gmail()