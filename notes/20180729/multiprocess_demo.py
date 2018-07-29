import os
import time
from multiprocessing import Pool

import requests


def download_url(name, url):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    res = requests.get(url)
    end = time.time()
    print('get html length %s Task %s runs %0.2f seconds.' % (len(res.text), name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    url_list = ['http://www.baidu.com'] * 10
    for i in range(len(url_list)):
        url = url_list[i]
        p.apply_async(download_url, args=(i, url,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
