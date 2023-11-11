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

# code start
desktop = GetDesktopWindow()
left, top, right, bottom = GetWindowRect(desktop)

def redraw(): # reset screen to normal. mostly removes all gdi effects.
  RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE | win32con.RDW_ALLCHILDREN)

def Melting(amt, minus):
  for i in range(amt):
    
