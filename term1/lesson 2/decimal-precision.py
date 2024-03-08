from decimal import Decimal, getcontext

''' 
  0.1 + 0.2 浮点计算结果使用二进制表示时为无限循环
  计算机字长有限后续字符按照 0 舍 1 入进行处理
'''

# 设置精度值
getcontext().prec = 5

# 先转字符串
print(Decimal(str(10)) / Decimal(str(3)))