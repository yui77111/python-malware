from base64 import b64encode
from Crypto.Cipher import AES
from lib.config import AES_IV, AES_KEY

"""
AES
除了MODE_SIV模式key长度为：32, 48, or 64,
其余key长度为16, 24 or 32
详细见AES内部文档
CBC模式传入iv参数
本例使用常用的ECB模式
"""


def initialization(k):
    if len(k) > 32:
        k = k[:32]
    return to16(k)

def to16(key):
    key = bytes(key, encoding="utf8")
    while len(key) % 16 != 0:
        key += b'\0'
    return key

def aesEncryptEcb(text):
    """
    默认无填充
    :param text: str, 原始字符串
    :return: str，返回base64
    """
    cipher = AES.new(initialization(AES_KEY), AES.MODE_ECB)
    result = cipher.encrypt(to16(text))
    return b64encode(result).decode()

def aesEncryptCbc(text):
    """
    默认无填充
    :param text: str, 原始字符串
    :return: str，返回base64
    """
    cipher = AES.new(initialization(AES_KEY), AES.MODE_CBC, AES_IV.encode())
    result = cipher.encrypt(to16(text))
    return b64encode(result).decode()