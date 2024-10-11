#!/usr/bin/env python3

import unittest
import subprocess

class test(unittest.TestCase):
    def test(self):
        try:
            res = subprocess.check_output("unbuffer make attack", shell=True)
        except subprocess.CalledProcessError as e:
            res = e.output
        print(res.decode(errors="replace"))
        self.assertTrue(b"root:" in res)


if __name__ == '__main__':
    unittest.main()

