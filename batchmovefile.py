#/bin/usr/python
#-*- coding:utf-8 -*-

import os,os.path
import re

__author__ = 'Francics'

'''
高效批量移动文件
'''

def movefile(suffix,inpath,outpath):
   '''
   suffix 文件后缀
   inpath 源文件夹路径的根目录 
   outpath 输出文件夹目录 
   根据输入的源文件家路径遍历其子目录下所有符合后缀的文件移动到
   输出文件夹目录
   '''
   if not os.path.exists(inpath):
      raise IOError('输入文件夹[%s]不存在' % inpath)
  
   if not os.path.exists(outpath):
      raise IOError('输出文件夹[%s]不存在' % outpath)
      
   for root, dirname, files in os.walk(inpath):
      for filename in files:
         m = re.search(r'.*\.'+suffix+r'$',filename)
         if m != None:
            oldpath = os.path.join(root,filename)
            newpath = os.path.join(outpath,filename)
            try:
               os.rename(oldpath,newpath)
            except FileExistsError as e:
               print("输出文件夹[%s]内存在文件[%s]" % (outpath,filename) )
               continue
   
if __name__ == '__main__':
   
   while True:
      inpath = input('请输入源文件夹路径:')
      if not os.path.exists(inpath):
         print("输入的文件夹不存在")
         continue
      outpath = input('请输入目标文件夹路径:')
      if not os.path.exists(outpath):
         print("输入的文件夹不存在")
         continue
      
      suffix = input('请输入文件后缀:')
      if re.search(r'\.',suffix) != None:
         print("文件后缀不需要输入符合'.'")
         continue      
      break  
   movefile(suffix,inpath,outpath1)
   
   
   