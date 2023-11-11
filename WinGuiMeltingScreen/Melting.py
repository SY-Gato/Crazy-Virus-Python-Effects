import ctypes
# REQUIRED: warning message
#ctypes.windll.user32.MessageBoxW(None, 'Hello', 'Hello World', 0)
print("WARNING! THIS PROGRAM CONTAINS INTENSE FLASHING LIGHTS AND GRAPHICAL EFFECTS (GDI).")
print("NOT FOR THE EPILEPTIC.")
print("")
continueconfirm = input('ARE YOU SURE YOU WOULD LIKE TO RUN THIS PROGRAM? [Y/N]:')
if continueconfirm == "Y" or continueconfirm == "y":
  continueconfirm2 = input('FINAL WARNING. NOT FOR THE EPILEPTIC. [Y/N]:')
  if continueconrirm2 != "Y" and continueconfirm2 != "y":
    quit()
else:
  quit()
# import required pywin32 modules for gdi
import win32api
import win32gui
import win32con
from win32gui import *
from win32gui import GetDesktopWindow,GetWindowDC,StretchBlt,BitBlt
from win32api import GetSystemMetrics
# import other helpful utilities
import random
import math
import time
import threading
# define metrics
hwnd = GetDesktopWindow()
hdc = GetWindowDC(hwnd)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
x2 = GetSystemMetrics(0)
y2 = GetSystemMetrics(1)
# define duplicates/variables for code
hwnd2 = hwnd
hdc2 = hdc

# code start
desktop = GetDesktopWindow()
left, top, right, bottom = GetWindowRect(desktop)

def redraw(): # reset screen to normal. mostly removes all gdi effects.
  RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE | win32con.RDW_ALLCHILDREN)

def Melting(amt, minus):
  for i in range(amt):
    hwnd2 = GetDesktopWindow()
    hdc2 = GetWindowDC(hwnd2)
    BitBlt(hdc2, 0, random.randint(0, 10)-minus, random.randint(0, x)-minus, y, hdc2, 0, 0, win32con.SRCCOPY)
    time.sleep(0.1)

curminus = 0
for i in range(30):
  Melting(5, curminus)
  curminus += 1
DeleteDC(hdc2)
redraw()
