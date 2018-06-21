# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 22:45:14 2018

@author: Mohammad
"""

import os.path
import cgi
from mako.template import Template

mytemplate = Template(filename='template.html')
print(mytemplate.render(name1='aaaa')) 
