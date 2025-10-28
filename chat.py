from ollama import chat
from os import system

history = [] # chatgpt's suggestion to store data

def chat_with_ai_stream(history:list) -> "generator":
    for streaming in chat(
            model="deepseek-coder:6.7b",
            messages=history,
            stream=1):
                temp = streaming['message']['content'] 
                text += temp 
                yield text

def chat_with_ai(some_message:str, stream:bool=1, hstory:bool=0) -> "response":
    try:
        text = ''

        if hstory:
            global history
            sample_ai = {'role':'assistant', 'content':''}
            sample_user = {'role':'user', 'content':some_message}
            history.append(sample_user)
        else:
            history = [{'role':'user', 'content':some_message}]

        if stream:
            chat_with_ai_stream(history)
        else:
            return chat(
                model="deepseek-coder:6.7b",
                messages=history)['message']['content'] 
        
        if hstory:sample_ai['content'] = text;history.append(sample_ai)

        return 0;

    except Exception as e:
        print(e)
        exit();

if __name__ == '__main__':
    # to check
    for streaming in chat(
                model="deepseek-coder:6.7b",
                messages=[{'role':'user', 'content':input()}],
                stream=1):
                    print(streaming['message']['content'], end="", flush=1)
