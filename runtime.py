import os
import sys
import subprocess
import json
import time
from colorama import Back, Style

global prevData, loopbackToModel
prevData = ""
loopbackToModel = ""

def commGPT(data):
    global prevData, loopbackToModel
    prevData = prevData+",NewData:"+data
    __commOS = 'python gpt_response.py \"'+str(prevData)+'\"'
    return subprocess.check_output(__commOS, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

def split_string(string):
    return [c for c in string]

if __name__ == "__main__":
    os.system("clear")
    print(Back.GREEN + " | ZeroneLabs | ♜ RunTime v2.0 | PaLM v2 | "+Back.BLACK)
    print("\n\n")
    while True:
        print(Back.BLACK)
        get_input = input(Back.BLUE+"♜ RunTime v2.0 | (⌐■_■)> "+Back.BLACK)
        if get_input == "clr_mem":
            prevData = ""
            os.system("tput bel")
            print(Back.RED+"Memory Reset !"+Back.BLACK)
            continue
        data = commGPT(get_input)
        loopbackToModel = data
        for i in split_string(data):
            if i != "`":
                time.sleep(0.005)
                sys.stdout.write("\033[1m"+i)
                sys.stdout.flush()
        if "```" in data:
            check_in = input("Script detected !, Run ? ( •_•) >")
            try:
                if check_in == "y" or check_in == "Y":
                    string_data = data.replace("```","")
                    if string_data.split("\n")[0].lower() == "bash":
                        print("Executing bash script")
                        writeTemp = open("TempScript.sh","a")
                        string_data = string_data.split("\n")
                        string_data.pop(0)
                        for i in string_data:
                            writeTemp.write(i+"\n")
                        writeTemp.close()
                        os.system("chmod +x TempScript.sh")
                        os.system("./TempScript.sh")
                        os.system("rm TempScript.sh")
                    if string_data.split("\n")[0].lower() == "python":
                        print("Executing Python script")
                        writeTemp = open("TempScript.py","a")
                        string_data = string_data.split("\n")
                        string_data.pop(0)
                        for i in string_data:
                            writeTemp.write(i+"\n")
                        writeTemp.close()
                        os.system("python TempScript.py")
                        os.system("rm TempScript.py")
                    if string_data.split("\n")[0].lower() == "c":
                        print("Executing C program")
                        writeTemp = open("TempScript.c","a")
                        string_data = string_data.split("\n")
                        string_data.pop(0)
                        for i in string_data:
                            writeTemp.write(i+"\n")
                        writeTemp.close()
                        print("Compiling Resource...")
                        os.system("gcc TempScript.c -o temp")
                        os.system("./temp")
                        os.system("rm TempScript.c")
                        os.system("rm temp")
                    else:
                        print("Executing bash script")
                        writeTemp = open("TempScript.sh","a")
                        string_data = string_data.split("\n")
                        for i in string_data:
                            writeTemp.write(i+"\n")
                        writeTemp.close()
                        os.system("chmod +x TempScript.sh")
                        os.system("./TempScript.sh")
                        os.system("rm TempScript.sh")
            except:
                #print(Back.GREEN + " | ZeroneLabs | ♜ RunTime v2.0 | PaLM v2 | "+Back.BLACK)
                print("/ ! \\")
        sys.stdout.write("\033[0m")
