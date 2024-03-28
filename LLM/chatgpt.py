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

    def llmResponse(self, user_prompt, query=0,  delim=";$;%"):
        if os.getenv("IS_DEMO"):
            # print("\nDEMO CHATGPT RES: ", prompts[query]['chat_gpt'])
            return prompts[query]['chat_gpt']
        else:
            ## ADD PIPELINE TO LLM##
            prompt = f"""Consider you are a Google Sheets expert with 5 years of experience. You know all the formulas and commands for the Google Sheets. You would be given a prompt  and your role is to return the formula for the prompt. If there are more than 1 formula then return as nested arrays: 

                    Prompt:{user_prompt}"""

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
