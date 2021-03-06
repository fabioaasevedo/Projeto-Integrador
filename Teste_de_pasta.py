# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:40:49 2020

@author: caio.mukai
"""
import pandas as pd
import cv2
import argparse
import numpy as np
import os
from os import listdir
from os.path import isfile, join, isdir
from processa import olha_imagem

start_path = os.getcwd()
os.chdir(start_path)
dir_image = ("/images/")
c = start_path +dir_image
folders = os.listdir(start_path+dir_image)

list_all_folder_dir = []
for name in folders:
    folder=os.path.join(start_path+dir_image,name)
    list_all_folder_dir.append(folder)
    
list_all_file_dir = []
for list_folder in list_all_folder_dir:
    os.chdir(list_folder)
    files = filter(os.path.isfile, os.listdir())
    files = [os.path.join(list_folder, f) for f in files]
    os.chdir(start_path)
    for teste in files:
        list_all_file_dir.append(teste)
list_all_itens = []
for _ in list_all_file_dir:
    itens = olha_imagem(_)
    list_all_itens.append(itens)

dfs = []
for i, value in enumerate(list_all_itens):
    df = pd.DataFrame(list_all_itens[i], columns=['ID','Class', 'Conf', 'Item'])
    dfs.append(df)
dfs = pd.concat(dfs, axis=0)
dfs = dfs.groupby(['ID','Item'], as_index=False)[['Conf']].max()
dfs.head()

