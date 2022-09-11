#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

PATH = '../texts'

def main():
    for fl in os.listdir(PATH):
        with open(os.path.join(PATH, fl)) as f:
            lines = f.readlines()
            
        with open(os.path.join(PATH, fl), 'w') as fw:
            for line in lines:
                if 'в" gr="S=obliq"></ana>' in line:
                    line = line.replace('вӧмми</w>', 'ӱмми</w>')
                fw.write(line)
    
    return 0

if __name__ == '__main__':
    main()
