import os
from dotenv import load_dotenv
from responses.dummy import prompts

from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()


class ChatGPT:
    def __init__(self):

        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        # print(self.OPENAI_API_KEY)

        self.openai_client = None
        self.openai_client = OpenAI(api_key=self.OPENAI_API_KEY)

    def llmResponse(self, res_dict, query=0,  delim=";$;%"):

        # prompt = f"""Consider you are a Google Sheets expert with 5 years of experience. You know all the formulas and commands for the Google Sheets. You would be given a prompt  and your role is to return the formula for the prompt. If there are more than 1 formula then return as nested arrays: 

        #             Prompt:{res_dict['user_prompt']}"""

        ### updated prompt
        prompt = f"""Consider you are a Google Sheets expert with 5 years of experience. You know all the formulas and commands for the Google Sheets. You would be given a prompt  and your role is to return the excel formula for the prompt. Donot try to complicate the formula. Simplicity is bliss. Always recheck the formula with a few sample examples if it's working or not. Apply COT. If there are more than 1 formula then add `$;%` as delimiter:

                    Meaning of the KEYWORDS:
                    FROM_SHEET: From where we are copying the data. Please make sure to include it in the formula where ever data is being read. If there is space in the given FROM_SHEET name then make sure to include a quotes in the formula otherwise it may throw an error.
                    TO_SHEET : Where we will store the data
                    OUTPUT_LOCS : The cell in the TO_SHEET where we will paste the formula.

                    Meta-data: {res_dict}
                    Prompt:{res_dict['user_prompt']}"""

        if os.getenv("IS_DEMO"):
            # print("\nDEMO CHATGPT RES: ", prompts[query]['chat_gpt'])
            return prompts[query]['chat_gpt']
        else:
            ## ADD PIPELINE TO LLM##

            if self.openai_client:
                response = self.openai_client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt},
                    ]
                )

                # print("\n\n", response.choices[0].message)
                ## CLEAN RESPONSE ##

                return response.choices[0].message  # need to update

            else:
                print("\n\n Initiate connection with OpenAI !! >> chatgpt.py")
