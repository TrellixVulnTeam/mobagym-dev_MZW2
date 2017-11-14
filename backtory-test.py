import requests
import json
from global_vars import *


# login function
def backtory_login():
    login_headers = {'X-Backtory-Authentication-Id': BACKTORY_AUTHENTICATION_ID,
                     'X-Backtory-Authentication-Key': BACKTORY_AUTHENTICATION_KEY}
    login_payload = {'username': USER_NAME, 'password': PASSWORD}
    login_r = requests.post("https://api.backtory.com/auth/login", data=login_payload, headers=login_headers)
    access_token = login_r.json()['access_token']
    expires_in = login_r.json()['expires_in']
    return access_token, expires_in


access_token, expires_in = backtory_login()

# upload file section
upload_headers = {'Authorization': 'Bearer' + ' ' + access_token, 'X-Backtory-Storage-Id': BACKTORY_STORAGE_ID}


file = {'fileItems[0].fileToUpload': open('img.jpg', 'rb')}
upload_data = {'fileItems[0].path': '/path1/', 'fileItems[0].replacing': True}


upload_r = requests.post("http://storage.backtory.com/files", data=upload_data, files=file, headers=upload_headers)
print()
print(upload_r)
print()
print(upload_r.json())
print()
output_link = "http://storage.backtory.com/files" + upload_r.json()['savedFilesUrls'][0]
print(output_link)

