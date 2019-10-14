#!python3
# mapIt.py -Launches a map in the browser using an address from the command line or clipboard.

import webbrowser
import sys
import pyperclip

print(sys.argv)
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.amap.com/search?query='+address)

