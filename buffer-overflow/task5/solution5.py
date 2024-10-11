#!/usr/bin/env python3
import sys
import struct

# make sure to use these functions to write strings or bytes (bytestring) so that the order is preserved
def writeStr(v):
    assert isinstance(v, str)
    sys.stdout.buffer.write(v.encode("ascii"))
    sys.stdout.flush()

def writeBytes(v):
    assert isinstance(v, bytes)
    sys.stdout.buffer.write(v)
    sys.stdout.flush()

def writeLong(v):
    assert isinstance(v, int)
    sys.stdout.buffer.write(v.to_bytes(8, 'little'))
    sys.stdout.flush()

# Use this to debug your attack.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Here we have the address of the main function.
pmain = int(sys.stdin.readline(), 16)
adr = pmain + 0x36 

#writeStr("1"*20) 
#writeLong(adr)
writeStr("pwd0\n")


# 0x55555555526a
# 0x5555555550b0
# 0x555555558010
# 0x0000555555555234
