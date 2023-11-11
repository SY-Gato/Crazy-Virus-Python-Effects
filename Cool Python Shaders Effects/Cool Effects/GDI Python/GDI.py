import win32api
import win32gui
import random
import win32con
from win32gui import *
from win32gui import GetDesktopWindow,GetWindowDC,StretchBlt,BitBlt
from win32api import GetSystemMetrics
from math import *
hwnd = GetDesktopWindow()
hdc2 = GetWindowDC(hwnd)
hdc3 = hdc2
hdc4 = hdc2
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
x2 = GetSystemMetrics(0)
y2 = GetSystemMetrics(1)


import math
import time
desktop = GetDesktopWindow()
left, top, right, bottom = GetWindowRect(desktop)

def redraw():
    RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE | win32con.RDW_ALLCHILDREN)

def radial_move(amt):
    for i in range(int(amt)):
        hdc = GetDC(0)
        memdc = CreateCompatibleDC(hdc)
        hbit = CreateCompatibleBitmap(hdc, x, y)
        sel = SelectObject(memdc, hbit)

        val = random.randint(1,2)
        rateofturning = 30
        print(val)
        if val == 1:

            PlgBlt(memdc, ((left-rateofturning, top+rateofturning), (right-rateofturning, top-rateofturning), (left+rateofturning, bottom+rateofturning)), hdc, 0, 0, x2, y2, 0, 0, 0)

    

        if val == 2:

            PlgBlt(memdc, ((left+rateofturning, top-rateofturning), (right+rateofturning, top+rateofturning), (left-rateofturning, bottom-rateofturning)), hdc, 0, 0, x2, y2, 0, 0, 0)

    
        AlphaBlend(hdc, random.randint(-10, 10), random.randint(-10, 10), x,  y, memdc, 0, 0, x, y, (0, 0, 70, 0))

        SelectObject(memdc, sel)
        DeleteObject(sel)
        DeleteObject(hbit)
        DeleteDC(memdc)
        DeleteDC(hdc)


def Sliding(amt):
    for i in range(int(amt)):

        hdc = GetDC(0)
        r = random.randint(0,1)
        if r == 1:
            for i in range(10):
                StretchBlt(hdc, 0, -50, x, y, hdc, 0, 0, x, y, win32con.SRCCOPY)
                StretchBlt(hdc, 0, y - 50, x, y, hdc, 0, 0, x, y, win32con.SRCCOPY)
                
        else:
            for i in range(10):
                StretchBlt(hdc, 0, 50, x, y, hdc, 0, 0, x, y, win32con.SRCCOPY)
                StretchBlt(hdc, 0, -y + 50, x, y, hdc, 0, 0, x, y, win32con.SRCCOPY)

cAmt = 0
def Melting(amt, minus):
    for i in range(amt):
        #BitBlt(hdc3, 0, random.randint(0, 10), random.randint(0, x), y, hdc3, 0, 0, win32con.SRCCOPY)
        BitBlt(hdc3, 0, random.randint(0-minus, 10-minus), random.randint(0-minus, x-minus), y, hdc3, 0, 0, win32con.SRCCOPY)
        time.sleep(0.10)


def HatchBrush():
    r = math.Random
    hdc4 = GetDC(0)
    mhdc = CreateCompatibleDC(hdc4)
    hbit = CreateCompatibleBitmap(hdc4, x, y)



for i in range(35):
    #radial_move(10)
    Melting(35, cAmt)
    cAmt -= 1
DeleteDC(hdc3)
redraw()