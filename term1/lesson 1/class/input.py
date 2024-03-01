# input 返回值类型永远是 str

# 算数推荐
# print(eval(input('input:')))

# 多组分割
sign = ' ' # 分割符号
arr = input('input:').split(sign)

for i in range(len(arr)):
  if ((arr[i].isdigit())):
    arr[i] = float(arr[i]) # 确保小数
  else:
    continue
print(arr)