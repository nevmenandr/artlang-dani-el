#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from bs4 import BeautifulSoup

PATH = '../texts'

def main():
    for fl in os.listdir(PATH):
        bs = BeautifulSoup(open(os.path.join(PATH, fl)), "xml")
        xml_content = bs.prettify()
        with open(os.path.join(PATH, fl), 'w') as fw:
            fw.write(xml_content)

    return 0

if __name__ == '__main__':
    main()
