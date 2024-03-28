import gspread


gc = gspread.oauth(
    credentials_filename='./credentials/credentials-oauth.json',
    authorized_user_filename='./credentials/oauth-user-credentials.json'
)

# sh = gc.open("Example spreadsheet")

# print(sh.sheet1.get('A1'))
