import os
from 中文代码 import 转译器

# 检查并创建配置文件
if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/config.txt"):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/config.txt", "w") as write_file:
        write_file.write("")

# 获取代码文件列表
with open(os.path.dirname(os.path.abspath(__file__)) + "/config.txt", "r") as config:
    file_list = list(config.read().split("\n"))

# 顺序执行代码
for file_path in file_list:
    # 注释
    if file_path.startswith("#") or file_path == "":
        pass
    else:
        # 如果文件存在
        if os.path.exists(file_path):
            转译器.文件路径(file_path)
        else:
            print(f"没有找到 {file_path} 文件")