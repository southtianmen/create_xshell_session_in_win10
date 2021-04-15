#!/usr/bin/env python3
# author:yl

'''
适用于xshell5，xshell6未测试过
'''

import base64
import os
from Cryptodome.Hash import SHA256
from Cryptodome.Cipher import ARC4
from base64 import *
from win32api import GetUserName


class xshell_secret():

    def __init__(self):
        # sid = [i.split(" ") for i in os.popen(r'whoami /user').read().split('\n') if
        #    GetUserName() in i][0][-1]
        self.sid = [i.split(" ") for i in os.popen(r'whoami /user').read().split('\n') if
           GetUserName() in i][0][-1]

    # 解密
    def decrypt_string(self, lpassowrd):
        v1 = base64.b64decode(lpassowrd)
        v3 = ARC4.new(SHA256.new(self.sid.encode('ascii')).digest()).decrypt(v1[:len(v1) - 0x20])
        if SHA256.new(v3).digest() == v1[-32:]:
            return v3.decode('ascii')
        else:
            return None

    # 加密
    def encrypt_string(self, spassowrd):
        spassowrd = bytes(spassowrd, encoding='utf8')
        sid = bytes(self.sid, encoding='utf8')
        # print(sid)
        cipher = ARC4.new(SHA256.new(sid).digest())
        checksum = SHA256.new(spassowrd).digest()
        ciphertext = cipher.encrypt(spassowrd)
        return b64encode(ciphertext + checksum).decode()

# 命令行模式
def get_args():
    import argparse
    parser = argparse.ArgumentParser(description='Process args for powering on a Virtual Machine')
    parser.add_argument('-e', '--encode', type=str, action='store')
    parser.add_argument('-d', '--decode', type=str, required=False, action='store')
    args = parser.parse_args()
    return args


def main():
    try:
        result = get_args()
        if result.encode and result.decode:
            print("Parameters -d or -e must not appear at the same time")
        elif result.encode:
            print(xshell_secret().encrypt_string(result.encode))
        elif result.decode:
            print(xshell_secret().decrypt_string(result.decode))
    except Exception as _:
        exit(100)

if __name__ == "__main__":
    main()

