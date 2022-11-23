# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:41:05 2022

@author: Bilge
"""

import pagan

inpt=input("Girin:")

img=pagan.Avatar(inpt,pagan.SHA512)

img.show()

outpath='output/'
filename=inpt+ ".png"
img.save(outpath,filename)