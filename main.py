from utils.gsheets import connectToWorkbookViaShare, updatePromptToSheet, connectToWorkbookViaOAuth
from utils.functions import fetchUserPrompt, clean_response
from LLM.chatgpt import ChatGPT


def runPipeline(LLM_model, workbook):

    toExit, res_dict = fetchUserPrompt()
    if not toExit:
        # need to get rid of query later on!!
        LLM_res = LLM_model.llmResponse(res_dict, query=1)
        LLM_res = clean_response(LLM_res)
        print('\n\nLLM RESPONSE : ', LLM_res)

        updatePromptToSheet(LLM_res,  workbook, res_dict)

    return toExit


def main():

    # ID of google sheet -- NEED to automate this!!
    # sheet_id = "1XiJIWkql-xGXdRy8fgy8OB3OTnj6ypxRBVAfR-5M_DU"

    # workbook, client = connectToWorkbookViaShare(sheet_id)
    workbook, client = connectToWorkbookViaOAuth()
    LLM_model = ChatGPT()

    toExit = False
    while not toExit:
        print("\n\n*************NEW COMMAND*************\nType q or quit to exit")
        toExit = runPipeline(LLM_model, workbook)


if __name__ == "__main__":
    main()
