#coding=utf-8
"""
Created on Mon Dec 29 13:36:37 2014

@author: Gavin
"""


import sys 
from pyquery import PyQuery as pq
from time import ctime
import time
import re
import os
import urllib.request

total_downloads = 0


def main(page_start, page_end):
    file_path_pre = 'F:/Download/Python/'
    folder_name = 'duan'
    page_url = 'http://jandan.net/' + folder_name + '/page-'
    folder_name = file_path_pre + folder_name + '/' + str(page_start) + '-' + str(page_end) + '.txt'
    t0 = time.time()    
    txt = open(folder_name, 'w', encoding='utf-8')
    txt.write('页面访问成功\n')
    for page_num in range(page_start,page_end + 1):
        crawl_page(page_url, page_num, folder_name, txt)
    
    txt.close()
    print('whole crawl time is ', time.time() - t0,'s')


def crawl_page(page_url, page_num, folder_name, txt):
    page_url = page_url + str(page_num)
    print('start handle', page_url)
    print('', 'starting at', ctime())
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Host': 'jandan.net'
    }
    t0 = time.time()

    # page_html = pq(url=page_url, headers=headers)  # 获取网页html
    req = urllib.request.Request(page_url, headers=headers)
    resp = urllib.request.urlopen(req)
    html = resp.read().decode('utf-8')
    page_html = pq(html)

    comment_id_patt = r'<li id="comment-(.+?)">'
    comment_ids = re.findall(comment_id_patt, page_html.html())
    fun_texts = {}
    for comment_id in comment_ids:
        fun_text = dispose_comment(page_html, comment_id)
        if fun_text: 
            fun_texts.update(fun_text)
    if not os.path.exists(folder_name):
        print('', 'new folder', folder_name)
        os.makedirs(folder_name)
    for fun_text in fun_texts.items():
        # save into txt      
        text = ('page-' + str(page_num) + fun_text[0] + '\n' + fun_text[1] + '\n\n')
        # print text
        txt.write(text)
    print('finished at', ctime(), ',total time', time.time()-t0, 's')


def dispose_comment(page_html,comment_id):
    fun_text_dict = {}
    id = '#comment-'+comment_id
    comment_html = page_html(id)
    oo_num = int(comment_html(id + ' .tucao-like-container span').text())
    xx_num = int(comment_html(id + ' .tucao-unlike-container span').text())
    oo_to_xx = oo_num/xx_num if xx_num != 0 else oo_num
    """
    if isinstance(fun_text, unicode): 
        #s=u"中文" 
        print(fun_text.encode('gb2312') 
    else: 
        #s="中文" 
        print(fun_text.decode('utf-8').encode('gb2312')
    """
    # if xx_num > 300 :
    if oo_num > 100 and oo_to_xx > 10:
        fun_text = comment_html(id + ' .text p').text()
        text_name = id + '_oo' + str(oo_num) + '_xx' + str(xx_num)
        fun_text_dict[text_name] = fun_text
        # print fun_text
    return fun_text_dict


if __name__ == '__main__':  
    # pic page not less than 4000
    # ooxx page not less than 900
    page_start = int(input('Input  start page number: '));
    page_end = int(input('Input  end   page number: '));
    main(page_start, page_end)


