import time
import datetime
import win32api
import win32con
from keycode import VK_CODE

log = open("C:/cygwin/var/log/numlock.log", "w")

state = win32api.GetKeyState(VK_CODE["num_lock"])
output = "%s state=%d" % (datetime.datetime.now(), state)
print output
log.write(output + "\n")

if state == 0:
    win32api.keybd_event(VK_CODE["num_lock"], 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(VK_CODE["num_lock"], 0, win32con.KEYEVENTF_KEYUP, 0)

state = win32api.GetKeyState(VK_CODE["num_lock"])
output = "%s state=%d" % (datetime.datetime.now(), state)
print output
log.write(output + "\n")

log.close()
