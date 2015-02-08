import mouse
import msvcrt
from keycode import *

class Event:

    def __init__(self, mouse):
        self.mouse = mouse

    def handle(self):

        control_arrow = 0xE0
        in_prev = 0

        while True:

            in_cur = ord(msvcrt.getch())
#             print "0x%02X" % (in_cur)
            found = False

            if in_prev == control_arrow:
                key_code = KEYCODE_ARROW
            else:
                key_code = KEYCODE

            for i in key_code:
                if in_cur == i[1]:
                    print i[0]
                    found = True
                    self.mouse.click(i[2], i[3])

            if found == False:
                if in_cur == KEYCODE_CONTROL["control+h"]:
                    print "control+h"
                elif in_cur == KEYCODE_CONTROL["control+q"]:
                    print "control+q"
                elif in_cur == KEYCODE_CONTROL["control+s"]:
                    print "control+s"

            in_prev = in_cur
