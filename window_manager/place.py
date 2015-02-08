# -*- coding: shift_jis -*-
import win32gui

def restore():

    hwnd = win32gui.FindWindow("Button", "スタート")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("Button", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 2, 860, 62, 38, True)
        print "Button"

    hwnd = win32gui.FindWindow("Shell_TrayWnd", "")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, -2, 856, 1444, 46, True)
        print "Shell_TrayWnd"

    hwnd = win32gui.FindWindow("ConsoleWindowClass", "place_save")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("ConsoleWindowClass", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 110, 125, 668, 484, True)
        print "ConsoleWindowClass"

    hwnd = win32gui.FindWindow("Alternate Owner", "")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("Alternate Owner", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 0, 0, 0, 0, True)
        print "Alternate Owner"

    hwnd = win32gui.FindWindow("IEFrame", "このページは表示できません - Internet Explorer")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("IEFrame", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 527, 11, 250, 339, True)
        print "IEFrame"

    hwnd = win32gui.FindWindow("MozillaWindowClass", "ページ読み込みエラー - Mozilla Firefox")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("MozillaWindowClass", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 6, 8, 516, 342, True)
        print "MozillaWindowClass"

    hwnd = win32gui.FindWindow("Alternate Owner", "")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("Alternate Owner", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 0, 0, 0, 0, True)
        print "Alternate Owner"

    hwnd = win32gui.FindWindow("#32770", "locate: すべてのファイル")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("#32770", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 975, 438, 453, 251, True)
        print "#32770"

    hwnd = win32gui.FindWindow("CabinetWClass", "window_manager")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("CabinetWClass", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 774, 9, 654, 420, True)
        print "CabinetWClass"

    hwnd = win32gui.FindWindow("mintty", "-bash")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("mintty", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 0, 360, 810, 488, True)
        print "mintty"

    hwnd = win32gui.FindWindow("Internet Explorer_Hidden", "")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("Internet Explorer_Hidden", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 0, 0, 0, 0, True)
        print "Internet Explorer_Hidden"

    hwnd = win32gui.FindWindow("Internet Explorer_Hidden", "")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("Internet Explorer_Hidden", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 0, 0, 0, 0, True)
        print "Internet Explorer_Hidden"

    hwnd = win32gui.FindWindow("Progman", "Program Manager")
    if hwnd == 0:
        hwnd = win32gui.FindWindow("Progman", None)
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, 0, 0, 1440, 900, True)
        print "Progman"

