# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:23:57 2018

@author: sivajrm
"""

import subprocess
def main():   
    proc=subprocess.Popen("notepad.exe", shell=False)
    return proc.pid

if __name__ == "__main__": 
    main();