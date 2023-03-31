from base64 import b64encode
from pyDes import des, CBC, PAD_PKCS5, ECB
from lib.config import DES_IV, DES_KEY

"""
des(key,[mode], [IV], [pad], [pad mode])
key:必须正好8字节
mode（模式）：ECB、CBC
iv:CBC模式中必须提供长8字节
pad:填充字符
padmode:加密填充模式PAD_NORMAL or PAD_PKCS5
"""



def desEncryptCbc(text):
    """
    填充默认使用pkcs5
    :param text: str, 原始字符串
    :return: str，返回base64
    """
    cipher = des(DES_KEY, CBC, DES_IV, pad=None, padmode=PAD_PKCS5)
    result = cipher.encrypt(text, padmode=PAD_PKCS5)
    return b64encode(result).decode()


def desEncryptEcb(text):
    """
    填充默认使用pkcs5
    :param text: str, 原始字符串
    :return:  str，返回base64
    """
    cipher = des(DES_KEY, ECB, pad=None, padmode=PAD_PKCS5)
    result = cipher.encrypt(text, padmode=PAD_PKCS5)
    return b64encode(result).decode()

