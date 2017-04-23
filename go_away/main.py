# -*- coding: utf-8 -*-

"""
    main
"""

import time
import utils
import config

"""
while True:
    time.sleep(config.REFRESH)
    print(50*"\n")
    url = config.URL
    samples = utils.parserHtml(utils.getInfo(url))
    for tram in samples:
        print(utils.clean(tram.text))
    print(1*"\n")
"""

from tkinter import *

fenetre = Tk()

url = config.URL
samples = utils.parserHtml(utils.getInfo(url))
test = ""
for tram in samples:
    test = test + utils.clean(tram.text) + "\n"
label = Label(fenetre, text=test)
# label.pack()
# fenetre.mainloop()

while True:
    time.sleep(5)
    samples = utils.parserHtml(utils.getInfo(url))
    test = ""
    for tram in samples:
        test = test + utils.clean(tram.text) + "\n"
    label = Label(fenetre, text=test)
    label.pack()
    fenetre.update_idletasks()
