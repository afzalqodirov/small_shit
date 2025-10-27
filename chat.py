from ollama import chat
from os import system

history = [] # chatgpt's suggestion to store data

def chat_with_ai(some_message:str) -> "response":
    try:
        text = ''

        global history
        sample_ai = {'role':'assistant', 'content':''}
        sample_user = {'role':'user', 'content':some_message}
        history.append(sample_user)

        for streaming in chat(
                model="deepseek-coder:6.7b",
                messages=history,
                stream=1):
                    temp = streaming['message']['content'] 
                    text += temp 
                    yield text

        sample_ai['content'] = text
        history.append(sample_ai)

        return 0;

    except Exception as e:
        print(e)
        exit();


if __name__ == '__main__':
    # to check
    for i in chat_with_ai(input()):
        print(i, end='', flush=1)
