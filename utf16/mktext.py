# -*- coding: shift_jis -*-

import struct

output = open("utf16.txt", "w")

data = ""

# byte order mark
data += struct.pack("H", 0xFEFF)

# ��   �{   ��
# 65E5 672C 8A9E
# data += struct.pack("H", 0x65E5)
# data += struct.pack("H", 0x672C)
# data += struct.pack("H", 0x8A9E)

# �A���r�A��
# 0641 0642 0644
data += struct.pack("H", 0x0641)
data += struct.pack("H", 0x0642)
data += struct.pack("H", 0x0644)


output.write(data)
output.close()
