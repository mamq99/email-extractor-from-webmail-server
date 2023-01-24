# WE ARE GOING TO USE IMAP AND EMAIL LIBRARIES TO EXTRACT EMAILS FROM THE SERVER
# WE NEED TO FIRST FIND THE IMAP SERVER DETAILS 

import imaplib
import email
import pandas as pd

#File path where csv will be outputted
filename = r"E:\all_emails.csv"
#Dataframe set which will take email, subject, and date.
df = pd.DataFrame(columns=['Email','Subject', 'Date'])

# server name, email address and password
imap_server = "[Your imap server]" #e.g., "mail.gmail.com"
email_address = "youremail@gmail.com"
password = "password123"    

#You can also use a variable here and take the password as a input from the user. 
# password = input("enter your password:")

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

#Selecting the mail box which we will search through
imap.select("Inbox")

# Setting up the search critera. The emails would go into the msgnums.
_, msgnums = imap.search(None, 'ALL')
print(msgnums) #All emails would be printed through this command

# setting up a loop which will go through each email and extract the requirement from each email: Subject, To, and Date
i=0
for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")

    message = email.message_from_bytes(data[0][1])

#     print(f"Message Number: {msgnum}")

#     Getting Subject
    subject = message.get('Subject')    
#     print(subject)
       
#     Getting To(recipiient)
    email_list = message.get('To')
#     print(email_list)

#   Getting Date
    email_date = message.get('Date')
    
    #Appending the data to the dataframe by row (in order)
    df.loc[len(df)] = [email_list, subject, email_date]
    # print(len(msgnums))

print(df)
df.to_csv(filename)

imap.close()
imap.logout()
