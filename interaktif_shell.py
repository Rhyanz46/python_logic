from time import sleep
import code
import os
import sys
import readline, rlcompleter


class Orang:
    nama = "arian"
    umur = 40

def testfunc():
    print("proes...")
    sleep(5)
    print("ok")



va = globals().copy()
va.update(locals())

shell= code.InteractiveConsole(va)

os.system('clear')
sys.ps1 = 'Perintah => '
readline.parse_and_bind("tab : complete")
shell.interact()

from random import  choice