from urllib import request
import json
import random


def drag_all():
    begin_id = 105091112
    all_articles = []
    flag = True
    while flag:
        a_drag_articles = drag_once(begin_id)
        if len(a_drag_articles) > 0:
            all_articles.extend(a_drag_articles)
            begin_id = a_drag_articles[-1].get('id')
        else:
            flag = False
    print('length of all articles is', len(all_articles))
    print(all_articles)
    return all_articles


def drag_once(begin_id):
    print(begin_id)
    post_params = 'containerid=0&maxid='+str(begin_id)+'&stickmaskid='
    with request.urlopen('https://www.meipian.cn/static/action/load_columns_article.php?userid=34954095',
                         data=post_params.encode('utf-8')) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        print('Data:', data.decode('utf-8'))
        articles = json.loads(data)
        return articles


def view(mask_id, times):
    url_prefix = 'https://www.meipian.cn/'
    article_url = url_prefix + mask_id
    k = 0
    while k < times:
        k = k + 1
        with request.urlopen(article_url) as f:
            # data = f.read()
            print(str(k), '.request url:', article_url, ',status:', f.status, f.reason)


def start():
    all_articles = drag_all()
    n = 0
    for article in all_articles:
        times = random.randint(100, 130);
        n = n + 1
        print(str(n), ':', 'id:', article.get('id'), 'mask_id:', article.get('mask_id'), ', view times:', str(times))
        view(article.get('mask_id'), times)


if __name__ == '__main__':
    start()

