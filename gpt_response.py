import os
import sys
import subprocess
import json
def __reqOut(chat_session):
    __commOS = 'curl -s -H "Content-Type: application/json" -d \'{ "prompt": { "text": \"Assistant:My name is rigel User:'+str(chat_session)+', Assistant :I should write the name of the programming language if im writing a script\"} }\' "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=AIzaSyC-g6QFIoAGlEMnf61v6iSbL5NJwbxnhEM"'

    if True :
        saveTemp = subprocess.check_output(__commOS, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        tempJsonWrite = open('temp.json','w')
        tempJsonWrite.write(saveTemp)
        tempJsonWrite.close()
        with open('temp.json') as f:
            return json.load(f)['candidates'][0]['output']
    

if __name__ == "__main__":
    try:
        print(__reqOut(sys.argv[1].replace("?","")))
    except:
        print("An Error Occured !")