# email-extractor-from-webmail-server
This email extractor extracts emails from the webmail server (it can be specific to any company). The requirement was to extract recipient email addresses from the webmail inbox.  

Task:
1. To fetch all email addresses of the recipient from the inbox.

Process:
1. Find the imap server name first and input it in the "imap_server".
2. input the your email address and password login.
   (you can ask the user to input it and store it in a variable for security purposes).
3. We will be using the imap4_ssl, you can change it to simple imap if it is required.          However, webmail does use ssl.
4. Select the category you want to search in, we will be using the "Inbox". You can change it to outbox or sent (whatever you wish).
5. If you wish to alter your searching criteria, you can change the "imap.search(None, 'ALL')" to "imap.search(None, '[insert search keyword]')".
6. Through the loop we iterate over each email and get the subject, recipient, and date; we save the fetched data into variable.
7. Save the variables into a dataframe.
8. print and output the data to a csv file.
9. Close and logout of the webmail.

Technology Used:
1. imaplib library
2. email library
3. pandas

Sources Used:
1. Visual Studio Code
2. Python
