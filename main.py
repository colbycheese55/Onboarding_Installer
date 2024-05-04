import requests
import subprocess
import json
import os

def download_file(url: str, save_path: str) -> bool:
    return True
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return True
        else:
            return False
    except Exception:
        return False

def run_cmd(cmd: str) -> bool:
    return True
    try:
        process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.returncode == 0
    except Exception:
        return False
    

# MAIN
with open("windows.json", "r") as file:
    instructions = json.load(file)

for instruction in instructions:
    print(instruction["text"]+":")

    if "path" in instruction and os.path.exists(os.path.expanduser(instruction["path"])):
        print("\tRequirement already fulfilled, \033[33mskipping\033[0m")
        continue

    if "skip_cmd" in instruction and run_cmd(instruction["skip_cmd"]):
        print("\tRequirement already fulfilled, \033[33mskipping\033[0m")
        continue

    if "download_URL" in instruction:
        url = instruction["download_URL"][0]
        save_path = instruction["download_URL"][1]
        result = download_file(url, save_path)
        if result:
            print("\tDownloaded \033[32msuccessfully\033[0m")
        else:
            print("\tDownload \033[31mfailed\033[0m")
            continue

    result = run_cmd(instruction["cmd"])
    if result:
        print("\tCommand executed \033[32msuccessfully\033[0m")
    else:
        print("\tCommand execution \033[31mfailed\033[0m")
        continue
    
        
