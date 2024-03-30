import gspread


gc = gspread.oauth(
    credentials_filename='./credentials/credentials-oauth.json',
    authorized_user_filename='./credentials/oauth-user-credentials.json'
)

# sh = gc.open("Example spreadsheet")

# print(sh.sheet1.get('A1'))


#
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
#
## OAuth scope for Google Sheets API
#scope = ['https://spreadsheets.google.com/feeds',
#         'https://www.googleapis.com/auth/drive']
#
## Path to your service account credentials JSON file
#credentials = ServiceAccountCredentials.from_json_keyfile_name('YOUR_SERVICE_ACCOUNT_FILE.json', scope)
#
## Authorize the credentials
#client = gspread.authorize(credentials)
#
## Open the Google Sheet by its ID
#sheet = client.open_by_key('YOUR_SHEET_ID')
#
## Select the worksheet where you want to write data
#worksheet = sheet.get_worksheet(0)  # index 0 represents the first sheet
#
## Write data to the worksheet
#data = [['Data1', 'Data2', 'Data3'],
#        ['Data4', 'Data5', 'Data6']]
#worksheet.append_rows(data)
