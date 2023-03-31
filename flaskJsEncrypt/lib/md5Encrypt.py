import hashlib


def md5Encrypt(text):
    """
    :param text: str, 原始字符串
    :return: str
    """
    if not isinstance(text, bytes):
        text = bytes(text, 'utf-8')
    m = hashlib.md5()
    m.update(text)
    return m.hexdigest()