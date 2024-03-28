import gspread
from google.oauth2.service_account import Credentials


def getSheetNames(workbook):
    return list(map(lambda x: x.title, workbook.worksheets()))


def testConnection(workbook):
    # ''' Might want to write some test and print connection status on the console '''
    print(getSheetNames(workbook))

    pass


def connectToWorkbookViaAouth():

    # Print connection name...

    # fetch all worksheet names
    # sheets = list(map(lambda x: x.title, workbook.worksheets()))
    # print(sheets)

    pass


def connectToWorkbookViaShare(sheet_id):

    scopes = [  # differnet access we might want
        "https://www.googleapis.com/auth/spreadsheets"
    ]

    creds = Credentials.from_service_account_file(
        "credentials/credentials.json", scopes=scopes)

    # Aurthorize
    client = gspread.authorize(creds)

    workbook = client.open_by_key(sheet_id)
    # print(workbook.worksheets())

    # ----TEST/PRINT CONNECTION----
    # testConnection(workbook)

    return workbook, client


def updatePromptToSheet(LLM_res, workbook, res_dict):

    # check if worksheet exists
    sheets_list = getSheetNames(workbook)
    OUTPUT_LOCS = res_dict['OUTPUT_LOCS'].split()
    TO_SHEET = res_dict['TO_SHEET']

    if TO_SHEET not in sheets_list:
        workbook.add_worksheet(title=TO_SHEET, rows=100, cols=20)

    if len(OUTPUT_LOCS) > 1:
        for op_cell, res in zip(OUTPUT_LOCS, LLM_res):  # check if both have same len
            workbook.worksheet(TO_SHEET).update_acell(op_cell, res)
    elif len(OUTPUT_LOCS) == 1:
        workbook.worksheet(TO_SHEET).update_acell(OUTPUT_LOCS[0], LLM_res[0])
    else:  # single cell
        workbook.worksheet(TO_SHEET).update_acell("A1", LLM_res[0])

    print("\n\nADDED!!\n")
