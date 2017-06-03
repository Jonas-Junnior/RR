import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
from numpy import *

path1 = r'C:\Users\TheJonasLegend\Desktop\PI Data\43\hsf_1'
path2 = r'C:\Users\TheJonasLegend\Desktop\PI Data\44\hsf_1'
path3 = r'C:\Users\TheJonasLegend\Desktop\PI Data\45\hsf_1'
path4 = r'C:\Users\TheJonasLegend\Desktop\PI Data\46\hsf_3'

path5 = r'C:\Users\TheJonasLegend\Desktop\PI Data\validation_set\C'
path6 = r'C:\Users\TheJonasLegend\Desktop\PI Data\validation_set\D'
path7 = r'C:\Users\TheJonasLegend\Desktop\PI Data\validation_set\E'
path8 = r'C:\Users\TheJonasLegend\Desktop\PI Data\validation_set\F'

listing = os.listdir(path1)
num_sample = size(listing)
print (num_sample)
img_rows, img_cols = 28, 28
for file in listing:
    im = Image.open(path1 + '\\' + file)
    img = im.resize((img_rows,img_cols))
    gray= img.convert('L')
    
    gray.save(path5 + '\\' + file, "PNG")
    
listing = os.listdir(path2)
num_sample = size(listing)
print (num_sample)
img_rows, img_cols = 28, 28
for file in listing:
    im = Image.open(path2 + '\\' + file)
    img = im.resize((img_rows,img_cols))
    gray= img.convert('L')
    
    gray.save(path6 + '\\' + file, "PNG")
    
listing = os.listdir(path3)
num_sample = size(listing)
print (num_sample)
img_rows, img_cols = 28, 28
for file in listing:
    im = Image.open(path3 + '\\' + file)
    img = im.resize((img_rows,img_cols))
    gray= img.convert('L')
    
    gray.save(path7 + '\\' + file, "PNG")
    
listing = os.listdir(path4)
num_sample = size(listing)
print (num_sample)
img_rows, img_cols = 28, 28
for file in listing:
    im = Image.open(path4 + '\\' + file)
    img = im.resize((img_rows,img_cols))
    gray= img.convert('L')
    
    gray.save(path8 + '\\' + file, "PNG")