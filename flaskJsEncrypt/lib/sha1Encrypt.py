import hashlib

def sha1Encrypt(text):
    """
    :param text: str, 原始字符串
    :return: str
    """
    if not isinstance(text, bytes):
        text = bytes(text, 'utf-8')
    sha = hashlib.sha1(text)
    encrypts = sha.hexdigest()
    return encrypts
