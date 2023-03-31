from base64 import b64encode
from Crypto.Cipher import DES3
from lib.config import DES3_IV, DES3_KEY

"""
new(key, mode, *args, **kwargs)
key:必须8bytes倍数，16/24不足末尾填充'\0'补足
mode：
iv:初始化向量适用于MODE_CBC、MODE_CFB、MODE_OFB、MODE_OPENPGP，4种模式
    ``MODE_CBC``, ``MODE_CFB``, and ``MODE_OFB``长度为8bytes
    ```MODE_OPENPGP```加密时8bytes解密时10bytes
    未提供默认随机生成
nonce：仅在 ``MODE_EAX`` and ``MODE_CTR``模式中使用
        ``MODE_EAX``建议16bytes
        ``MODE_CTR``建议[0, 7]长度
        未提供则随机生成
segment_size：分段大小，仅在 ``MODE_CFB``模式中使用，长度为8倍数，未指定则默认为8
mac_len： 适用``MODE_EAX``模式，身份验证标记的长度（字节），它不能超过8（默认值）
initial_value：适用```MODE_CTR```，计数器的初始值计数器块。默认为**0**。
"""


def initialization(k):
    len_k = len(k)
    if len_k > 24:
        k = k[:24]
    else:
        while len(k) < 16:
             k += " "
    return k.encode()

def des3EncryptCbc(text):
    """
    填充默认使用pkcs5
    :param text: str, 原始字符串
    :return: str，返回base64
    """
    iv = DES3_IV.encode('utf-8')
    pad = lambda x: x + (8 - len(x) % 8) * chr(8 - len(x) % 8)
    raw = pad(text).encode('utf-8')
    cipher = DES3.new(initialization(DES3_KEY), mode=DES3.MODE_CBC, iv=iv)
    result = cipher.encrypt(raw)
    return b64encode(result).decode()

def des3EncryptEcb(text):
    """
    填充默认使用pkcs5
    :param text: str, 原始字符串
    :return: str，返回base64
    """
    pad = lambda x: x + (8 - len(x) % 8) * chr(8 - len(x) % 8)
    raw = pad(text).encode('utf-8')
    cipher = DES3.new(initialization(DES3_KEY), DES3.MODE_ECB)
    result = cipher.encrypt(raw)
    return b64encode(result).decode()