import gspread  # library provides high level abstraction for g-sheet manupilation tasks
from google.oauth2.service_account import Credentials
from utils.functions import updatePrompt, extract_keywords

scopes = [  # differnet access we might want
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file(
    "./credentials/credentials.json", scopes=scopes)

# Aurthorize
client = gspread.authorize(creds)

# ID of google sheet -- NEED to automate this!!
sheet_id = "1XiJIWkql-xGXdRy8fgy8OB3OTnj6ypxRBVAfR-5M_DU"

workbook = client.open_by_key(sheet_id)
# print(workbook.worksheets())

# Test connection
# fetching the 1st row of `Sheet1` => row 1
# values1 = workbook.sheet1.row_values(1)
# print('\n\n', values1)

# values2 = workbook.sheet1.get("A1:A3")
# print('\n\n', values2)

# values3 = workbook.worksheet("data").get("A1:B14")  # select worksheet by name
# print('\n\n', values3)

# fetch all worksheet names
# sheets = list(map(lambda x: x.title, workbook.worksheets()))
# print(sheets)

# Update the cells:
# workbook.worksheet("Sheet1").update_acell("A1", "UPDATED VALUE!!")

# check if formula works:
# workbook.worksheet("data").update_acell("B16", "=SUM(B1:B14)")

###### --- FEED USER INPUT --- ######
# user_prompt = """In the given table A1:B14 find the mean, median and mode for both columns A and B FROM_SHEET data TO_SHEET data OUTPUT_LOCS A16, A17, A18, B16, B17, B18"""
# user_prompt = "Generate a dummy dataset for market sales of pizza with attributes location, prices and quantity TO_SHEET data2"

user_prompt = input('\n\nENTER THE PROMPT:')

# user prompt
keywords = ["FROM_SHEET", "TO_SHEET", "OUTPUT_LOCS"]

# TO_SHEET = ""
# GPT_PROMPT = ""
# FROM_SHEET = ""
# OUTPUT_LOCS = ""

# FROM_SHEET, TO_SHEET, OUTPUT_LOCS = cleanPrompt(user_prompt, keywords)   # move inside updatePrompt


# FETCHING DATA from Chatgpt for multiple formulas and introducing my delimiters:
# PROMPT_TEMPLATE = <prompt>

delim = ";$;%"

###### --- CASE 1 --- ######
# user_prompt = """In the given table A1:B14 find the mean, median and mode for both columns A and B FROM_SHEET data TO_SHEET data OUTPUT_LOCS A16, A17, A18, B16, B17, B18"""


# # chatGPT response
# res = """=AVERAGE(A1:A14);$;%=MEDIAN(A1:A14);$;%=MODE.SNGL(A1:A14);$;%
# =AVERAGE(B1:B14);$;%=MEDIAN(B1:B14);$;%=MODE.SNGL(B1:B14)""".split(delim)

# # print(extract_keywords(user_prompt, keywords))

# # update values
# updatePrompt(res,  workbook, user_prompt, keywords)

###### --- CASE 2 --- ######

user_prompt = "Generate a dummy dataset for market sales of pizza with attributes location, prices and quantity TO_SHEET data2"


# # chatGPT response
res = """={{"Location", "Prices", "Quantity"};
 {"New York", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"Los Angeles", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"Chicago", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"Houston", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"Phoenix", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"Philadelphia", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"San Antonio", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"San Diego", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"Dallas", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"San Jose", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"Austin", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"Jacksonville", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
 {"Fort Worth", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)}}
""".split(delim)

# print(extract_keywords(user_prompt, keywords))

###### --- PRINT RESPONSE --- ######

print('\n\nCHATGPT RESPONSE: ', res)


# update values
updatePrompt(res,  workbook, user_prompt, keywords)
