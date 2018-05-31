import random
import asyncio
import aiohttp
from urllib import request
import json


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


async def view(mask_id, times):
    print('======', 'mask_id:', mask_id, ', view times:', str(times))
    url_prefix = 'https://www.meipian.cn/'
    article_url = url_prefix + mask_id
    for seq in range(1, times):
        print('view the %s %d times...' % (article_url, seq))
        async with aiohttp.request('GET', article_url) as f:
            print('%s. %s status: %s %s' % (str(seq), article_url, f.status, f.reason))


def start():
    all_articles = drag_all()
    tasks = [view(article.get('mask_id'), random.randint(5, 10)) for article in all_articles]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    start()

