import random
import string
from datetime import datetime


# 加花干扰函数
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


# 生成测试数据
num_array = [random.randint(1, 100) for i in range(100)]
str_array = [''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) for i in range(10)]
float_array = [round(random.uniform(-100, 100), 2) for i in range(100)]
translation_dict = {"hello": "你好", "world": "世界", "python": "nb"}


def translate(word):
    if word in translation_dict:
        return translation_dict[word]
    else:
        return None
