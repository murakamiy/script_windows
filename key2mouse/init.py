# -*- coding: shift_jis -*-

import win32con
import win32gui
import win32process
import mouse


def callback(hwnd, proc_list):
    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        pid = win32process.GetWindowThreadProcessId(hwnd)
        title = win32gui.GetWindowText(hwnd)
        proc_list.append((hwnd, pid, title))
    return True

def init():
    proc_list = []
    win32gui.EnumWindows(callback, proc_list)

    for p in proc_list:
        if p[2] == "電卓":
            (left, top, right, bottom) = win32gui.GetWindowRect(p[0])
#             print left, top, right, bottom
            win32gui.MoveWindow(p[0], 0, 0, right - left, bottom - top, True)

    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowText(hwnd, "key2mouse")
    win32gui.MoveWindow(hwnd, 250, 0, 400, 400, True)

    m = mouse.Mouse(hwnd)
    return m
