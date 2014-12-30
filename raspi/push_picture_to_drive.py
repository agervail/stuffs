#!/usr/bin/python

from datetime import datetime
import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage


# Copy your credentials from the console
CLIENT_ID = 'BITE'
CLIENT_SECRET = 'CUL'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Path to the file to upload
FILENAME = 'uh.jpg'


storage = Storage('creds.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  # Run through the OAuth flow and retrieve credentials
  flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE,
                             redirect_uri=REDIRECT_URI)
  authorize_url = flow.step1_get_authorize_url()
  print 'Go to the following link in your browser: ' + authorize_url
  code = raw_input('Enter verification code: ').strip()
  credentials = flow.step2_exchange(code)
  storage.put(credentials)



# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
  'title': 'pic_' + datetime.now().strftime('%y-%m-%d_%H-%M'),
  'description': 'A test document',
  'mimeType': 'image/jpeg',
  'parents' : [{
    'kind': 'drive#fileLink',
    'id': '0B1uVehMk_uX7NUJhaWJ3TVR1SHc'
  }]
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
#pprint.pprint(file)
