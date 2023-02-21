from requests import request
from json import loads
from sys import argv
from os import path

class SMMS(object):
    def __init__(self,token):
        self.token = token
        self.ua = {'user-agent': 'smms/0.0.1'}
        self.api = 'https://sm.ms/api/v2/'

    # def get_token(self):
    #     url = self.api+'token'
    #     data = {
    #         'username': self.username,
    #         'password': self.password
    #     }
    #     r = request('POST',url, headers={**self.ua}, data=data)
    #     r_json = loads(r.text)
    #     if r_json['success']:
    #         print('[+] Get token success')
    #         self.api = r_json['data']['token']
    #     else:
    #         print('[-] Get token fail')
    #         exit(0)

    def upload_image(self,upload_file):
        url = self.api+'upload'
        r = request('POST', url, headers={**self.ua,'Authorization': self.token}, files={'smfile': open(upload_file, 'rb')})
        r_json = loads(r.text)
        print(r_json['data']['url'])
        return r_json['data']['url']

    # def get_upload_history(self):
    #     url = self.api+'/upload_history'
    #     r = request('GET',url,headers={**self.ua,'Authorization': self.token})
    #     r_json = loads(r.text)
    #     print(r_json)
    #     return r_json

    # def del_file(self,file_hash):
    #     url = self.api+'delete/{}'.format(file_hash)
    #     r = request('GET',url,headers={**self.ua,'Authorization': self.token})
    #     r_json = loads(r.text)
    #     if r_json['success']:
    #         print(r_json['message'])
    #     else:
    #         print('[-] File delete fail.')



def main():
    token = 'xxxxxxxxxxxxxxxxxxx'
    smms = SMMS(token)
    # smms.get_token()
    # smms.get_upload_history()
    # smms.del_file('LTQqltsKJV7OI6bD5GuMSmU1aR')
    if len(argv) >= 2:
        smms.upload_image(argv[1])
    else:
        print('[-] Example:{} <file>'.format(path.split(__file__)[-1]))


if __name__ == '__main__':
    main()