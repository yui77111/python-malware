## flaskJsEncrypt

flask框架搭建的加密器，用于前端js加密的爆破

### 1 前言

参考[jsEncrypter](https://github.com/c0ny1/jsEncrypter)，burp插件传输payload到*phantomjs*中启动前端加密函数对数据进行加密，但本地加密payload也是使用js，需要有一定的js基础。过程是burp传参到web，web再处理参数返回，所以使用python实现了个类似的。

### 2 安装依赖

```
python3 -m pip install -r requirements.txt
```

### 3 加密类型

##### 3.1 目前实现

- url编码
- base64
- md5
- hmac
- sha1
- sha256
- sha384
- sha512
- rsa
- aes - ecb/cbc
- des - ecb/cbc
- des3 - ecb/cbc

### 4 使用

##### 4.1 flask

根据审计前端js，获取加密方式和所需的key/iv

修改`flaskJsMain.py`中对应

![image-20221009165735853](https://s2.loli.net/2022/10/09/6REXn5esQqh8cMP.png)

修改`/lib/config.py`中对应

![image-20221009165454488](https://s2.loli.net/2022/10/09/WxeOhcIrFJzPZwV.png)

运行

```
python3 flaskJsMain.py
```

![image-20221009164131682](https://s2.loli.net/2022/10/09/rfEzwJ6VLCBYunR.png)

##### 4.2 burp

加载插件*jsEncrypter.0.3.2.jar*

![image-20221009163920515](https://s2.loli.net/2022/10/09/YkZers9dD1mBpNF.png)

点击Connect，查看是否成功连接，再点击Test测试加密，成功返回

![image-20221009164334823](https://s2.loli.net/2022/10/09/EmOZwWJgc1VhLAx.png)

爆破，选择*Intruder*下*Payloads*的*Payload Processing*添加由插件处理

![image-20221009170646062](https://s2.loli.net/2022/10/09/logFOQx78TWwIfh.png)

start

![image-20221009171734695](https://s2.loli.net/2022/10/09/TpYXbmZzsyrPRlB.png)