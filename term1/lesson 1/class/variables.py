# 六大基本数据类型

# 数字
print(int(2)) # 整数
print(float(2)) # 浮点数
print(complex(2, 3)) # 复数

# 字符串 str
print(str('abc'))
print(str("abc"))
print(str("abc'123'")) # 字符串嵌套

# 列表 list
arr = list((4, 2, 6))
print(arr)
print(len(arr)) # 列表长度
print(sorted(arr, reverse=True)) # 列表排序 - 返回新列表
arr.sort(reverse=True)  # 列表排序 - 原地排序
print(arr)
arr.append('a') # 原列表尾追加 单元素
arr.extend(['b', 'c', 'd']) # 原列表尾追加 多元素
print(arr)

# 元组
tup = (1, 2, 3)

# 集合
my_set1 = set()
my_set2 = { 1, 2, 3 }
print(my_set2)

# 字典
dict1 = dict()
dict2 = { 1: "a", 2: "b" }
print(dict1, dict2)
# {} 默认为 dict 字典类型
