## sendgmail.py 
The google API needs 2 files 
 - client_secret.json in homedir 
 - gmail-python.json in ~/.credentials/ : created first time opens authentication in webbrowser

See also https://developers.google.com/drive/v3/web/quickstart/python

### Installation Step 1: Turn on the Drive API
1. Use the [Wizard](https://console.developers.google.com/start/api?id=drive) to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
1. On the Add credentials to your project page, click the Cancel button.
1. At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
1. Select the Credentials tab, click the Create credentials button and select OAuth client ID.
1. Select the application type Other, enter the name "Drive API Quickstart", and click the Create button.
1. Click OK to dismiss the resulting dialog.
1. Click the file_download (Download JSON) button to the right of the client ID.
1. Move this file to your working directory and rename it client_secret.json.



### Installation Step 2: Install the Google Client Library
1. Run the following command to install the library using pip:
1. ```pip install --upgrade google-api-python-client```
1. See the library's [installation page](https://developers.google.com/api-client-library/python/start/installation) for the alternative installation options.
