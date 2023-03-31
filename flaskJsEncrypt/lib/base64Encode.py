from base64 import b64encode

def base64Encode(text):
    """
    :param text: str, 原始字符串
    :return: str
    """
    if not isinstance(text, bytes):
        text = bytes(text, 'utf-8')
    return b64encode(text).decode()