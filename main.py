import email
import imaplib

user_name = "emailId"
password = "appPassword"

mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
mail.login(user_name,password)
print(mail.list())
mail.select('"[Gmail]/Sent Mail"')


result, data = mail.uid('search', None, '(HEADER Subject "Subject")')

# # '(HEADER Subject "Presentation")'
inbox_list = data[0].split()
# # recent = inbox_list[-1]
# # oldest = inbox_list[0]
#

for email_list in inbox_list:
#
    result2, email_data = mail.uid('fetch', email_list, '(RFC822)')
#
    raw_email = email_data[0][1].decode("utf-8")
#
    email_message = email.message_from_string(raw_email)
    # print(email_message['To'])
#     print(email_message['From'])
    print(email_message['Subject'])
    payload = email_message.get_payload()

    try:
        print(payload[0])
    except Exception as ex:
        print(ex)
        pass
#