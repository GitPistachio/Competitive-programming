# Project name : SPOJ: BINARYIO - Binary Input and Output
# Author       : Wojciech Raszka
# Date created : 2019-03-10
# Description  :
# Status       : Accepted (23380003)
# Comment      :

import sys
import struct
from math import log

inp = sys.stdin.buffer.read()
no_of_ret = len(inp)//8
sys.stdout.buffer.write(struct.pack("%sd" % no_of_ret, *(list(map(lambda x: log(x), struct.unpack("%sd" % no_of_ret, inp))))))
