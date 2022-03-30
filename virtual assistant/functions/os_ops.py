import os
import subprocess as sp

paths ={
    'notepad': "C:\\WINDOWS\\system32\\notepad.exe",
    'browser': "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])

def open_browser():
    os.startfile(paths['browser'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])