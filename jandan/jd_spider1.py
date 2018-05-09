# -*- coding = UTF-8 -*-
'''
目标：煎蛋网妹子图
2018/4/22
环境：pyhton3
https://www.cnblogs.com/protogenoi/p/8881182.html

http://www.tendcode.com/article/jiandan-meizi-spider/
http://www.tendcode.com/article/jiandan-meizi-spider-2/
'''

import urllib.request  # 使用url处理包，urllib.request模块是用来打开和读取URLs的
import re  # 使用正则表达式
import hashlib  #
import base64  #
from bs4 import BeautifulSoup  #
import time  # time
import logging  # log
import sys  #

'''
下载单张图片到制定的文件夹下
'''


def load_img(imgurl, file):
    name = imgurl.split('/')[-1]
    item = urllib.request.urlretrieve('http:' + imgurl, \
                                      # 'E:\\Spider\\74172\\Pictures\\jandan2\\%s'%(name))
                                      file + '\\%s' % (name))
    print(name + ' is loaded')


'''
md5加密
'''


def _md5(value):
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()


'''
bash64解码
注意 原字符串长度报错问题
'''


def _base64_decode(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)


'''
解密获取图片链接
'''


def get_imgurl(m, r='', d=0):
    e = "DECODE"
    q = 4
    r = _md5(r)
    o = _md5(r[0:0 + 16])
    n = _md5(r[16:16 + 16])
    l = m[0:q]
    c = o + _md5(o + l)
    m = m[q:]
    k = _base64_decode(m)
    h = list(range(256))
    b = [ord(c[g % len(c)]) for g in range(256)]

    f = 0
    for g in range(0, 256):
        f = (f + h[g] + b[g]) % 256
        tmp = h[g]
        h[g] = h[f]
        h[f] = tmp

    t = ""
    p, f = 0, 0
    for g in range(0, len(k)):
        p = (p + 1) % 256
        f = (f + h[p]) % 256
        tmp = h[p]
        h[p] = h[f]
        h[f] = tmp
        t += chr(k[g] ^ (h[(h[p] + h[f]) % 256]))
    t = t[26:]
    return t


'''
获取关键字符串
'''


def get_r(js_url):
    js_respon = urllib.request.urlopen(js_url)
    js = js_respon.read().decode('utf-8')
    _r = re.findall('c=[\w\d]+\(e,"(.*?)"\)', js)
    return _r


'''
获取一个页面的所有图片的链接
'''


def get_urls(url, pages, file):
    page = 0
    imagNum = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Host': 'jandan.net'
    }
    #########################################
    while page < pages:
        req = urllib.request.Request(url, headers=headers)
        respon = urllib.request.urlopen(req)
        html = respon.read().decode('utf-8')
        ##########################################
        js_url = 'http:' + re.findall('<script src="(//cdn.jandan.net/static/min/[\w\d]+\.\d+\.js)"></script>', html)[
            -1]
        _r = get_r(js_url)[0]
        soup = BeautifulSoup(html, 'lxml')
        tags = soup.select('.img-hash')
        for tag in tags:
            img_hash = tag.text
            img_url = get_imgurl(img_hash, _r)
            print(imagNum, '------>', img_url)
            imagNum = imagNum + 1
            load_img(img_url, file)
        ############################################
        nextUrl = re.findall(r'Older Comments" href=".+?.#comments"', html)[0]
        print('page#', 90 - page, '---->done!')
        url = 'http:' + nextUrl[22:-1]
        page += 1
        time.sleep(10)
    print('done all!')
    print('located---->', file)


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx/'
    pages = 2
    file = 'E:\\Spider\\ooxx'
    get_urls(url, pages, file)
