

import os#operating system
from pathlib import Path
import logging #built in package
print(">> Script started running...")

#Creating basic login configuration this will track the time of a code execution and show the message given
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')
logging.getLogger().setLevel(logging.INFO)


#Providing the list of files I want to have:

list_of_files=[
    "src/__init__.py",#Constructor file :where different function can be called and files can be imported for overall functionality(this is called modular coding)
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipnb",#jupyter notebook file:The entire project will be based on that which will be then converted to modular coding
    "test.py"
]
for filepath in list_of_files:
    filepath=Path(filepath)#This helps to run the code in any operating system.Because different os has their default way of filepaths.Using the Path library adjusts the filepath according to the OS
    filedir,filename=os.path.split(filepath)#filedir is the folder

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)#folder creation
        logging.info(f"Creating directory;{filedir} for the file:{filename} ")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"{filepath} already exists")        