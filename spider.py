# -*- coding: utf-8 -*-

import requests
import re
import time
from requests.exceptions import ReadTimeout, HTTPError, RequestException

for n in range(1, 169):
    a_url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_'+str(n)+'.html'
    # print(a_url)
    try:
        html_1 = requests.get(a_url)
        # print(html_1.status_code)
    except ReadTimeout:
        print('html_1 timeout')
    except HTTPError:
        print('html_1 httperror')
    except RequestException:
        print('html_1 reqerror')
        n = n - 1
        continue

    html_1.encoding = 'GB18030'
    # print(html_1.text)
    detailList = re.findall('<a href="(.*?)" class="ulink">', html_1.text)
    # print(detailList)
    for m in detailList:
        b_url = 'http://www.dytt8.net'+m
        # print(b_url)

        while True:
            try:
                html_2 = requests.get(b_url)
                print(html_2.status_code)
                break
            except ReadTimeout:
                print('html_2 timeout')
            except HTTPError:
                print('html_2 httperror')
            except RequestException:
                print('html_2 reqerror')

        html_2.encoding = 'GB18030'
        # print(html_2.text)
        movieFtp = re.findall('<a href="(.*?)">.*?</a>.*?</td>', html_2.text)
        # print(movieFtp[0])
        time.sleep(0.01)
        with open('dytt.txt', 'a', encoding='utf-8') as fileTxt:
            if movieFtp.__len__() > 0:
                print(str(n)+':'+movieFtp[0])
                fileTxt.write(movieFtp[0]+'\n')
            else:
                print(b_url)



