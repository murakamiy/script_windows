import win32api, win32con, win32gui
import time

class Mouse:

    def __init__(self, hwnd, push_time = 0):
        self.push_time = push_time
        self.hwnd = hwnd

    def set_click_time(self, push_time):
        self.push_time = push_time

    def click(self, x, y):
        (ox, oy) = win32api.GetCursorPos()

        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(self.push_time)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,   x, y, 0, 0)

        win32api.SetCursorPos((ox, oy))
        win32gui.SetForegroundWindow(self.hwnd)
