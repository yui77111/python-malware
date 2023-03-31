from urllib import parse

def urlEncode(text):
    """
    :param text: str, 原始字符串
    :return: str
    """
    return parse.quote(text)