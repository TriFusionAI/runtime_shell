import os
import sys
import subprocess
import time
from colorama import Back
import threading
import shutil

global anim, prevData
prevData = ""
anim = 1
def clear_memory():
    global prevData, loopbackToModel
    prevData = ""
    loopbackToModel = ""
    os.system("tput bel")
    print(Back.RED + "Memory Reset !" + Back.BLACK)

def commGPT(data):
    global prevData, loopbackToModel, anim
    prevData = contextBreakDown(prevData+data)
    __commOS = 'python sysFiles/gpt_response.py \"'+str(prevData)+'\"'
    return subprocess.check_output(__commOS, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

def contextBreakDown(data):
    __commOS = 'python sysFiles/cbs.py \"'+data+'\"'
    return subprocess.check_output(__commOS, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

def execute_script(language, script_content):
    script_file_name = f"TempScript.{language.lower()}"
    executable_name = "temp"

    print(f"Executing {language} script")

    with open(script_file_name, "w") as write_temp:
        script_lines = script_content.split("\n")[1:]
        for line in script_lines:
            write_temp.write(line + "\n")

    if language.lower() == "c":
        print("Compiling Resource...")
        os.system(f"gcc {script_file_name} -o {executable_name}")
        os.system(f"./{executable_name}")
    elif language.lower() == "python":
        print("Initializing Python Interpreter...")
        os.system(f"python {script_file_name}")
        #os.system(f"./{executable_name}")
    else:
        os.system(f"chmod +x {script_file_name}")
        os.system(f"./{script_file_name}")

    os.system(f"rm {script_file_name}")

def loading_animation():
    global anim
    x = 0
    while True:
        if anim == 0:
            print("Runtime is processing the input",end='')
            print("", end='', flush=True)
            time.sleep(0.5)
            if x <= 3:
                x+=1
                print("."*x, end='', flush=True)
            else :
                x = 0
            print('\033[K', end='', flush=True)  # Clear the line from the cursor position to the end
            print('\r', end='', flush=True)
        else:
            time.sleep(0.5)
            continue

#run_loading_animation()
if __name__ == "__main__":
    os.system("clear")
    terminal_width, _ = shutil.get_terminal_size()
    current_line_length = 0
    print(Back.GREEN + " | ZeroneLabs | ♜ RunTime v3.0 |  Gemini-Pro | Experimental | " + Back.BLACK)
    print("\n\n")
    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()
    while True:
        print(Back.BLACK)
        get_input = input(Back.BLUE + "USER > " + Back.BLACK)
        #run_loading_animation(1)
        #loading_thread.join()
        print("\n" + Back.BLUE + "RunTime | ZrnLBS | (⌐■_■) \n" + Back.BLACK, end="")
        anim = 0

        try:
            if get_input == "clr_mem":
                anim = 1
                clear_memory()
                continue

            data = commGPT(get_input)
            anim = 1
            time.sleep(0.8)
            print("\n")
            loopbackToModel = data
            for char in data:
                if char != "`":
                    # current_line_length += 1
                    # if current_line_length >= terminal_width:
                    #     sys.stdout.write("\n")
                    #     sys.stdout.flush()
                    #     current_line_length = 0
                    time.sleep(0.01)
                    sys.stdout.write("\033[1m" + char)
                    sys.stdout.flush()
            if "```" in data:
                script_data = data.replace("```", "")
                script_language = script_data.split("\n")[0].lower()

                if script_language in ["bash", "python", "c"]:
                    execute_script(script_language, script_data)
                else:
                    execute_script("bash", script_data)
        except:
            print("/!\\")
            anim = 1