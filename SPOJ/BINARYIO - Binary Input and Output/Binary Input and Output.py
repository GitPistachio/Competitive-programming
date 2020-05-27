# Project name : SPOJ: BINARYIO - Binary Input and Output
# Author       : Wojciech Raszka
# Date created : 2019-03-10
# Description  :
# Status       : Accepted (23379972)
# Comment      :

import sys
import struct
from math import log

for block in iter(lambda: sys.stdin.buffer.read(8), ""):
    if block:
        x = log(struct.unpack("d", block)[0])
        sys.stdout.buffer.write(struct.pack("d", x))
    else:
        break
