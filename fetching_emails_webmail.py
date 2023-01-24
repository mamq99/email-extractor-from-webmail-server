# WE ARE GOING TO USE IMAP AND EMAIL LIBRARIES TO EXTRACT EMAILS FROM THE SERVER
# WE NEED TO FIRST FIND THE IMAP SERVER DETAILS 

import imaplib
import email
import pandas as pd

filename = r"E:\Abdul Manan\Undelivered Emails Zohad\Undelivered_emails.csv"
df = pd.DataFrame(columns=['Email','Subject', 'Date'])

imap_server = "mail.tradeforesight.com"
email_address = "nasir.ali@tradeforesight.com"
password = "alibabakhan123" 

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

_, msgnums = imap.search(None, 'ALL')
print(msgnums)

i=0
for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")

    message = email.message_from_bytes(data[0][1])

    print(f"Message Number: {msgnum}")
    
    subject = message.get('Subject')    
    print(subject)
       
    email_list = message.get('To')
    print(email_list)

    email_date = message.get('Date')
    
    df.loc[len(df)] = [email_list, subject, email_date]
    # print(len(msgnums))

print(df)
df.to_csv(filename)

imap.close()
imap.logout()
