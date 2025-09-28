num_str = input("请输入一个5位数字: ")

# 验证输入是否为5位数字
if len(num_str) != 5 or not num_str.isdigit():
    print("输入错误: 请输入5位数字")
else:
    # 判断是否为回文数
    if num_str == num_str[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
