#!/usr/bin/env python3

import itertools
import crypto

def infer_plaintext(msg, m):
    # Probing cache lines to find which ones were accessed 
    accessedCacheLines = []
    for line in range(crypto.cache_lines):
        address = line * crypto.cache_line_size
        _, t = m.read_address(address)
        if t == 1:
            accessedCacheLines.append(line)

    # Sets for possible l0 and r0 values
    possible_values_l0 = set()
    possible_values_r0 = set()

    # Encrypted ciphertext values
    l2 = ord(msg[0])
    r2 = ord(msg[1])

    for line in accessedCacheLines:
        startAddress = line * crypto.cache_line_size
        endAddress = (line + 1) * crypto.cache_line_size

        # Possible values of l0
        for address in range(startAddress, endAddress):
            possible_l0 = l2 ^ crypto.T[address]  
            possible_values_l0.add(chr(possible_l0))

        # Possible values of r0
        for address in range(startAddress, endAddress):
            r0_candidate = r2 ^ crypto.T[address]  
            possible_values_r0.add(chr(r0_candidate))

    return possible_values_l0, possible_values_r0

