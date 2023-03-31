import hmac
from lib.config import HMAC_KEY


def hmacEncrypt(text):
    """
    :param text: str, 原始字符串
    :return: str
    """
    key = HMAC_KEY
    if not isinstance(HMAC_KEY, bytes):
        key = bytes(HMAC_KEY, 'utf-8')
    if not isinstance(text, bytes):
        text = bytes(text, 'utf-8')
    h = hmac.new(key, text, digestmod='MD5')
    return h.hexdigest()
