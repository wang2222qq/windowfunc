#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'Francics'

from codecs import open
import os.path

def DelFileLine(filename,bgnline,endline):
   '''
   parament:
      filename
      bgnline  int  待删除文件的开始行数
      endline  int  待删除文件的结束行数
   '''
   if not isinstance(bgnline,int):
      raise TypeError('bgnline must be int')
   
   if not isinstance(endline,int):
      raise TypeError('endline must be int')
   
   try:
      with open(filename,'rb') as f:
         lines = f.readlines()
   except FileNotFoundError :
      print('文件:[%s]不存在' % filename)
      raise
      
   del lines[bgnline:endline]
   open(filename,'wb').writelines(lines)
   
if __name__ == '__main__':
  
   while True:
      filename = input("请输入文件路径:")
      if not os.path.exists(filename):
         print("输入的文件路径不存在")
         continue
      bgnline = input('请输入要删除文件中的起始行:')
      if not isinstance(bgnline,int):
         print("请输入数字")
         continue
      
      endline = input('请输入要删除文件中的结束行:')
      if not isinstance(endline,int):
         print("请输入数字")
         continue      
      break  
      
   DelFileLine(filename,bgnline,endline)
   