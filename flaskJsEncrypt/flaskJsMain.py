# -*- coding: utf-8 -*-

from flask import Flask, request
from lib.urlEncode import urlEncode
from lib.base64Encode import base64Encode
from lib.md5Encrypt import md5Encrypt
from lib.sha1Encrypt import sha1Encrypt
from lib.sha256Encrypt import sha256Encrypt
from lib.sha384Encrypt import sha384Encrypt
from lib.sha512Encrypt import sha512Encrypt
from lib.hmacEncrypt import hmacEncrypt
from lib.rsaEncrypt import rsaEncrypt
from lib.aesEncrypt import aesEncryptEcb, aesEncryptCbc
from lib.desEncrypt import desEncryptEcb, desEncryptCbc
from lib.des3Encrypt import des3EncryptEcb, des3EncryptCbc

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    str = request.form.get('payload')
    if str:
        # 加密方式
        # return urlEncode(urlEncode(rsaEncrypt(str)))
        return md5Encrypt(md5Encrypt(str) + 'salt')
    else:
    	return '^_^\n\rhello jsEncrypter!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1664)