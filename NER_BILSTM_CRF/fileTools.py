# -*- coding: UTF-8 -*-

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os
import re
import json
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    fileName=[]
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        fileName.append(child)
    return fileName

# 读取文件内容并打印
def readFile(filename):
    fopen = open(filename, 'r')  # r 代表read
    for eachLine in fopen:
        fileContent=eachLine
    try:
        content=json.loads(fileContent)["content"]
    except:
        content="$"
    content=re.sub("\s+","",content)
    fopen.close()
    return content





