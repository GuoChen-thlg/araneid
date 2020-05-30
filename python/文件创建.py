# -*- coding: utf-8 -*-
import os


def newFolder(folderPath):
    """
    创建文件夹


    folderPath : 文件夹路径
    """
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

