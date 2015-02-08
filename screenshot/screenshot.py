import os
import sys
import time
import struct
import win32api
import win32con
import win32clipboard
from keycode import VK_CODE

work_dir = "C:/Users/ya/Desktop/cygwin/tmp/screenshot"
arg = sys.argv[1]

if arg == "capture_all":

    print "capture_all"

    win32api.keybd_event(VK_CODE["print_screen"], 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(VK_CODE["print_screen"], 0, win32con.KEYEVENTF_KEYUP, 0)

elif arg == "capture_window":

    print "capture_window"

    win32api.keybd_event(VK_CODE["alt"], 0, 0, 0)
    win32api.keybd_event(VK_CODE["tab"], 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(VK_CODE["tab"], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE["alt"], 0, win32con.KEYEVENTF_KEYUP, 0)

    win32api.keybd_event(VK_CODE["alt"], 0, 0, 0)
    win32api.keybd_event(VK_CODE["print_screen"], 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(VK_CODE["print_screen"], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE["alt"], 0, win32con.KEYEVENTF_KEYUP, 0)


win32clipboard.OpenClipboard()
bitmap_data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
win32clipboard.EmptyClipboard()
win32clipboard.CloseClipboard()

try:
    os.stat(work_dir)
except OSError:
    os.mkdir(work_dir)

bitmap_size = len(bitmap_data)
bitmap_file_name = "%s/%03d.bmp" % (work_dir, len(os.listdir(work_dir)) + 1)
print "file=%s size=%d " % (bitmap_file_name, bitmap_size)
bitmap_file = open(bitmap_file_name, "wb")


header = ""
header += struct.pack("B", 0x42)                # file type
header += struct.pack("B", 0x4D)                # file type
header += struct.pack("I", bitmap_size + 14)    # file size
header += struct.pack("I", 0)                   # reserved
header += struct.pack("I", 14 + 40)             # offset: BITMAPFILEHEADER + BITMAPINFOHEADER

bitmap_file.write(header)
bitmap_file.write(bitmap_data)
bitmap_file.close()

# time.sleep(10)
