from urllib import request
from bs4 import BeautifulSoup


def repeatRequestUrl(url, times):
    req = request.Request(url);
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

    n = 0
    while n < times:
        with request.urlopen(req) as f:
            print(str(n), ':Status:', f.status, f.reason)
            n = n + 1
            #for k, v in f.getheaders():
            #    print('%s: %s' % (k, v))
            #print('Data:', f.read().decode('utf-8'))

if __name__ == '__main__':
    print('program started')
    with request.urlopen('https://www.meipian.cn/c/34954095') as f:
        data = f.read()
        print('Main Page Status:', f.status, f.reason)
        print('Data:', data.decode('utf-8'))
        soup = BeautifulSoup(data.decode('utf-8'), 'lxml')
        a_tags = soup.select("div.articleinfo a")
        print(a_tags)
        for a in a_tags:
            print(a.attrs)