#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import sys

def revert_text_to_html(link):
    """retern html from text

    - link : url from sys.args
    """
    text_data = urllib.urlopen(link).read()
    result = ''
    for string in text_data:
        string = string.replace(' ', '&nbsp;')
        string = string.replace('\n', '<br />\n')
        result = result + string

    return result

if __name__ == '__main__':
    print revert_text_to_html(sys.argv[1])