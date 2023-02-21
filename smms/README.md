## smms

在用`Typora`编写文本时，实现图片粘贴后自动上传到`smms`图床并返回url

### 设置

注册登录自己的[smms](https://sm.ms/)

生成`Secret Token`

![image-20210424152031380](https://i.loli.net/2021/04/24/Tbh3nSrZMOyWpg8.png)

将`Secret Token`替换脚本中的token值

```python
def main():
    token = 'xxxxxxxxxxxxxxxxxxxxx'
    smms = SMMS(token)
    if len(argv) >= 2:
        smms.upload_image(argv[1])
    else:
        print('[-] Example:{} <file>'.format(path.split(__file__)[-1]))
```

然后打开`Typora`偏好设置，按如下设置后，点击验证图片，看是否上传成功

![image-20210424151606268](https://i.loli.net/2021/04/24/fnulwJGWYK3t2QE.png)