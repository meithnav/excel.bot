import re
from LLM.chatgpt import ChatGPT


def extract_keywords(user_prompt, keywords):
    pattern = r'\b(' + '|'.join(keywords) + \
        r')\s+(.+?)(?=\s+(?:' + '|'.join(keywords) + r')|$)'
    matches = re.findall(pattern, user_prompt)
    result = {keyword: '' for keyword in keywords}

    for match in matches:
        result[match[0]] = match[1].strip()

    return result



def clean_response(LLM_res, delim=";$;%"):
    value_list = LLM_res.split(delim)
    updated_list = []
    for value in value_list:
        updated_value = value.replace('\n', '').strip()
        updated_list.append(updated_value)
    return updated_list


def fetchUserPrompt(keywords=["FROM_SHEET", "TO_SHEET", "OUTPUT_LOCS"]):

    user_prompt = input('\n\nENTER THE PROMPT:')
    if user_prompt not in ['q', 'quit']:
        dict = extract_keywords(user_prompt, keywords)
        dict['user_prompt'] = user_prompt

        print('\n\nEXTRACTED KEYWORDS : ', dict)

        return False, dict

    return True, {}

