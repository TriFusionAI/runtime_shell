import os
import sys
import json
import requests

def __reqOut(chat_session):
    url = "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=AIzaSyC-g6QFIoAGlEMnf61v6iSbL5NJwbxnhEM"
    headers = {"Content-Type": "application/json"}

    prompt = {
        "prompt": {
            "text": "Assistant:My name is rigel User:" + str(chat_session)
        }
    }

    response = requests.post(url, headers=headers, json=prompt)
    response_data = response.json()
    return response_data['candidates'][0]['output']

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            print(__reqOut(sys.argv[1].replace("?", "")))
        else:
            print("Usage: python script.py <chat_session>")
    except:
        print(Back.RED+"Critical Internal Error Occured while communicating with the Model !, Please Retry :("+Back.BLACK)
