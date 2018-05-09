# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 13:36:37 2014

@author: Gavin
"""

from pyquery import PyQuery as pq
from time import ctime
import time
import re
import os
import urllib

total_downloads = 0


def main(page_start, page_end, flag):
    file_path_pre = 'F:/Download/Python/'
    folder_name = 'ooxx' if flag else 'pic'
    page_url = 'http://jandan.net/' + folder_name + '/page-'
    folder_name = file_path_pre + folder_name + '/' + str(page_start) + '-' + str(page_end) + '/'
    t0 = time.time()    
    for page_num in range(page_start,page_end + 1):
        crawl_page(page_url, page_num, folder_name)
    print('whole crawl time is ', time.time() - t0, 's')


def crawl_page(page_url, page_num, folder_name):
    page_url = page_url + str(page_num)
    print('start handle', page_url)
    print('', 'starting at', ctime())
    t0 = time.time()
    page_html = pq(url=page_url)  # 获取网页html
    comment_id_patt = r'<li id="comment-(.+?)">'
    comment_ids = re.findall(comment_id_patt, page_html.html())
    name_urls = {}
    for comment_id in comment_ids:
        name_url = dispose_comment(page_html, comment_id)
        if name_url: 
            name_urls.update(name_url)
    if not os.path.exists(folder_name):
        print('', 'new folder', folder_name)
        os.makedirs(folder_name)
    for name_url in name_urls.items():
        file_path = folder_name + 'page-' + str(page_num) + name_url[0]
        img_url = name_url[1]
        if not os.path.exists(file_path) and file_path.endswith('.gif'): 
            print('', 'start download', file_path)
            print('', 'img_url is', img_url)
            urllib.urlretrieve(img_url, file_path)
        else:
            print('', file_path, 'is already downloaded')
    print('finished at', ctime(), ',total time', time.time()-t0, 's')


def dispose_comment(page_html, comment_id):
    name_url_dict = {}
    id = '#comment-'+comment_id
    comment_html = page_html(id)
    oo_num = int(comment_html(id + ' #cos_support-' + comment_id).text())
    xx_num = int(comment_html(id + ' #cos_unsupport-' + comment_id).text())
    oo_to_xx = oo_num/xx_num if xx_num != 0 else oo_num
    if oo_num > 300 and oo_to_xx > 7:
        imgs = comment_html(id + ' img')
        for i in range(0, len(imgs)):
            org_src = imgs.eq(i).attr('org_src')
            src = imgs.eq(i).attr('src')
            img_url = org_src if org_src else src
            if img_url:
                img_suffix = img_url[-4:]
                if not img_suffix.startswith('.'):
                    img_suffix = '.jpg'
                img_name = id + '_oo' + str(oo_num) + '_xx' + str(xx_num) + (('_' + str(i)) if i != 0 else '') + img_suffix
                name_url_dict[img_name] = img_url
            else:
                print('***url not exist')
    return name_url_dict


if __name__ == '__main__':  
    # pic page not less than 4000
    # ooxx page not less than 900
    page_start = int(input('Input  start page number: '))
    page_end = int(input('Input  end   page number: '))
    is_ooxx = int(input('Select 0: wuliao 1: meizi 2: funny '))
    main(page_start, page_end, is_ooxx)

