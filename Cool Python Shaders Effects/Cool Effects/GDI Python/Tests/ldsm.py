import ctypes
import random
import time
import win32api
import win32con
import win32gui
import win32ui

# Constants
TARGET_RADIUS = 50
TARGET_SPEED = 5

# Get screen dimensions
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Create target class
class Target:
    def __init__(self):
        self.x = random.randint(TARGET_RADIUS, screen_width - TARGET_RADIUS)
        self.y = random.randint(TARGET_RADIUS, screen_height - TARGET_RADIUS)
        self.dx = random.choice([-1, 1]) * TARGET_SPEED
        self.dy = random.choice([-1, 1]) * TARGET_SPEED

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off screen edges
        if self.x <= TARGET_RADIUS or self.x >= screen_width - TARGET_RADIUS:
            self.dx *= -1
        if self.y <= TARGET_RADIUS or self.y >= screen_height - TARGET_RADIUS:
            self.dy *= -1

    def draw(self, hdc):
        dc = win32ui.CreateDCFromHandle(hdc)
        brush = win32ui.CreateBrush(0, win32con.RGB(255, 255, 255), 0)
        pen = win32ui.CreatePen(win32con.PS_SOLID, 1, win32con.RGB(255, 0, 0))

        dc.SelectObject(brush)
        dc.SelectObject(pen)
        dc.Ellipse((self.x - TARGET_RADIUS, self.y - TARGET_RADIUS,
                    self.x + TARGET_RADIUS, self.y + TARGET_RADIUS))

# Window procedure
def wndProc(hWnd, message, wParam, lParam):
    if message == win32con.WM_PAINT:
        hdc, paintStruct = win32gui.BeginPaint(hWnd)
        
        Target.update()
        Target.draw(hdc)

        win32gui.EndPaint(hWnd, paintStruct)
        return 0

    elif message == win32con.WM_DESTROY:
        win32gui.PostQuitMessage(0)
        return 0

    return win32gui.DefWindowProc(hWnd, message, wParam, lParam)
#Register window class
className = 'BouncingTarget'
wndClass = win32gui.WNDCLASS()
wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
wndClass.lpfnWndProc = wndProc
wndClass.hInstance = win32api.GetModuleHandle(None)
wndClass.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
wndClass.lpszClassName = className
wndClassAtom = win32gui.RegisterClass(wndClass)

# Create window
hwnd = win32gui.CreateWindow(wndClassAtom, 'Bouncing Target', win32con.WS_OVERLAPPEDWINDOW,
                             win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
                             screen_width, screen_height, 0, 0, wndClass.hInstance, None)

# Show window
win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
win32gui.UpdateWindow(hwnd)

# Create target instance
target = Target()

# Message loop
#msg = win32gui.MSG()
#while win32gui.GetMessage(msg, hwnd, 0, 0):
    #win32gui.TranslateMessage(msg)
    #win32gui.DispatchMessage(msg)
    #time.sleep(0.01)