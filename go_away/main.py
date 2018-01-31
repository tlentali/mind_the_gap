# -*- coding: utf-8 -*-

"""
    main
"""
import logging
import time

import schedule

import config
from tbm import TbmParser

L = logging.getLogger(__name__)
L.setLevel(logging.DEBUG)
L.addHandler(logging.StreamHandler())


def get_tramway_schedule():
    L.info('Create TBM object')
    start = time.time()

    parser = TbmParser(config.URL)
    parser.parse()

    end = time.time()

    L.info('Done in {:.2f} sec'.format(end - start))
    print(parser.info)


def main():
    L.info('Lets go!')
    schedule.every(config.REFRESH).seconds.do(get_tramway_schedule)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
