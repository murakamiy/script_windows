# -*- coding: shift_jis -*-
import win32gui
import time


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

f = open("place.py", "w")

text = """\
# -*- coding: shift_jis -*-
import win32gui

def restore():

"""
f.write(text)

for p in proc_list:
    clazz   =  p[1]
    title   =  p[2]
    x       =  p[3]
    y       =  p[4]
    width   =  p[5]
    height  =  p[6]
    print clazz

    text = """\
    hwnd = win32gui.FindWindow("%s", "%s")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("%s", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, %d, %d, %d, %d, True)
        print "%s"

""" % (clazz, title, clazz, x, y, width, height, clazz)
    f.write(text)

f.close()
time.sleep(10)
