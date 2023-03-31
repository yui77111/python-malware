from base64 import b64encode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from lib.config import RSA_PUBLICKEY


def handlePubKey(key):
    """
    添加公钥头尾
    :param key: str
    :return: str
    """
    start = '-----BEGIN PUBLIC KEY-----\n'
    end = '-----END PUBLIC KEY-----'
    result = ''
    divide = int(len(key) / 64)
    divide = divide if (divide > 0) else divide+1
    line = divide if (len(key) % 64 == 0) else divide+1
    for i in range(line):
        result += key[i*64:(i+1)*64] + '\n'
    result = start + result + end
    return result


def rsaEncrypt(text):
    """
    :param text: str, 原始字符串
    :return: str, 返回base64
    """
    pub_key = handlePubKey(RSA_PUBLICKEY)
    pub = RSA.import_key(pub_key)
    cipher = PKCS1_v1_5.new(pub)
    result = cipher.encrypt(text.encode(encoding='utf-8'))
    return b64encode(result).decode()
