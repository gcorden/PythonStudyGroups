#!/usr/bin/env python3
'''Code snippet attempting to extract variable-level metadata from DDI Codebook XML'''

import xmltodict as xml
import pprint
from collections import OrderedDict

'''File to parse'''
xml_file = "edit_ddi38900-0001.xml"
xml_read = open(xml_file, 'r')

'''Create ordered dict from file
 Force creation of lists even when only one parameter'''
xml_dict = xml.parse(xml_read.read(), force_list=('catgry',))['codeBook']['dataDscr']['var']

for var in xml_dict:
    varname = var['@name']
    print(f"Name: {var['@name']}")
