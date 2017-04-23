# -*- coding: utf-8 -*-

"""
    blend of main and function, temporary.
"""

import time
import utils


while True:
    time.sleep(15)
    print(50*"\n")
    url = 'https://www.infotbm.com/nextdeparture/B/stoparea/TBT5529/backward'
    samples = utils.parserHtml(utils.getInfo(url))
    for tram in samples:
        print(utils.clean(tram.text))
    print(1*"\n")
