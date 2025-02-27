import os

print("Initializing the installtion...")
os.system("pip install google-generativeai")
os.system("pip install spacy")
#os.system("pip install subprocess")
os.system("pip install colorama")
os.system("pip install textblob")

print("\n\nTesting Runtime Context Breakdown system...")
workers = input("Enter the number of cores in your CPU (Default : 2):")
open("sysFiles/workers.zttf","w").write(workers)
os.system("python sysFiles/cbs.py 'runtime context breakdown system check'")

print("\n\nTesting gpt response output")
api = input("Enter Google AI Studio API (You can retrieve this from https://makersuite.google.com/app/apikey for free):")
open("sysFiles/api.txt","w").write(api)
os.system("python sysFiles/gpt_response.py 'Introduce yourself'")

print("\n\n!!! Check complete, to run the program, To start the system, type :python runtime.py !!!")
print("\nIf any issues occured while setting up the workers or the API, re-run this script to reconfigure...")
print("\n\nZeroneLabs\n\n") 