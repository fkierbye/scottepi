#!/usr/bin/python

# inspiration from here: https://developers.google.com/gmail/api/quickstart/python

from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
import sys
import getopt
import argparse
from apiclient import errors

# Parser for my command-line arguments
myparent = argparse.ArgumentParser(add_help=False)
group = myparent.add_argument_group('standard')
myparent.add_argument("-t","--emailTo", help="To email address", required=True)
myparent.add_argument("-f","--emailFrom", help="From email address", required=True)
myparent.add_argument("-s","--emailSubject", help="The email subject", required=True)
myparent.add_argument("-b","--emailBody", help="The email body", required=True)

try:
    flags = argparse.ArgumentParser(parents=[tools.argparser, myparent]).parse_args()
except ImportError:
    flags = None

#print(flags)

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python.json
SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'ScotteGmailer'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
	sender: Email address of the sender.
	to: Email address of the receiver.
	subject: The subject of the email message.
	message_text: The text of the email message.

    Returns:
	An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    #print(message)

    return {'raw': base64.urlsafe_b64encode(message.as_string())}

def main():
    """Send email via Gmail API."""

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    msg = create_message(flags.emailTo, flags.emailFrom, flags.emailSubject, flags.emailBody)

    try:
	service.users().messages().send(userId='me', body=msg).execute()
	print ("Message sent")
    except errors.HttpError, error:
	print ('An error occurred: %s' % error)

if __name__ == '__main__':
    main()
