# -*- coding: shift_jis -*-
import win32con
import win32gui


def callback(hwnd, proc_list):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        (left, top, right, bottom) = win32gui.GetWindowRect(hwnd)
        x = left
        y = top
        width = right - left
        height = bottom - top
        title = win32gui.GetWindowText(hwnd)
        clazz = win32gui.GetClassName(hwnd)
        proc_list.append((hwnd, clazz, title, x, y, width, height))
    return True


proc_list = []
win32gui.EnumWindows(callback, proc_list)

for p in proc_list:
    print p[1], p[2], p[3], p[4], p[5]
