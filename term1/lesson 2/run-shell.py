'''
使python 读取cmd 文件并执行 cmd 命令
'''
# 1. os.system(命令)
# 2. os.popen(命令, 模式(默认读))
#    返回一个与当前执行命令相关的对象，使用其read 方法读取命令返回值
#    已弃用，推荐使用subprocess.Popen
# 3. subprocess

import os
import subprocess

fileObj = open('./comd.cmd', mode= 'r', encoding='utf8') # 读取指令文件
command_arr = fileObj.read().split('\n') # 分割单行指令
command_arr = [shell for shell in command_arr if len(shell) > 0] # 过滤空指令

# 1.
# for item in command_arr:
#   os.system(item)


# 2.
# for item in command_arr:
#   res = os.popen(item, 'r')
#   res_read = res.read()
#   if (res_read):
#     print(res_read)

# 3. 
for item in command_arr:
  process = subprocess.Popen(item, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
  if (stderr):
    print('err:', stderr.decode('utf-8'))
  if (stdout):
    print('out:', stdout.decode('utf-8'))