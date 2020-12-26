from pydrive.auth import GoogleAuth 

# Authentification
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

from time import gmtime, strftime
import os
import smtplib, ssl

from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)

path = input("Enter the path of to the folder that you want to upload.")
#Test directory: /Users/nguyenthieukhang/ggdrive_automatic_upload/folder1
recieve = input("Enter your email address: ")

extension = input("Enter the extension (.<extension>) which you want to upload (Enter NO if not specified)")

email_message = 'Subject: Files Uploading Finished\n'

for x in os.listdir(path):  
    
    if(extension != "NO" and not (x.endswith(extension))): continue
        
    file_name = strftime("%Y-%m-%d_%H:%M:%S_", gmtime())+x
    f = drive.CreateFile({'title': file_name}) 
    try:
        f.SetContentFile(os.path.join(path, x)) 
        f.Upload() 
        email_message += (x + ' has been successsfully uploaded.\n')
    except: continue
    f = None
    
email_message += '\n' + 'vefhomework\n'
username = 'vefhomework@gmail.com'
password = 'webcreateaccount?service'

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    server.sendmail(username, recieve, email_message)

print("Uploading successful.")