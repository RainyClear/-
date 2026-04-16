import os
import re

# 主函数
def 文件路径(path):
    if not os.path.exists(os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/Code"):
        os.mkdir(os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/Code")
    # 脚本路径
    file_path_old = path.replace("\\", "/")
    # 脚本名字
    file_name = list(file_path_old.split("/"))[-1].replace(".txt", ".py")
    # 转译后的文件地址
    file_path_new = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/Code/" + file_name
    with open(file_path_old, "r") as code_content:
        code_content = code_content.read()
        
    # 替换代码
    code_content = re.sub(r'输出\s*=>(.*)', r'print("\1")', code_content)
    code_content = re.sub(r'变量\s*:\s*(.*?)\s*:(.*)', r'\1 = \2', code_content)
    code_content = re.sub(r'输入\s*=>(.*)', r'input("\1")', code_content)
    
    # 替换变量
    while True:
        math = re.search(r'(f?)"(.*?)%\$(.*?)\$%(.*?)"', code_content)
        if math:
            code_content = code_content.replace(f'{math.group(1)}"{math.group(2)}%${math.group(3)}$%{math.group(4)}"', f'f"{math.group(2)}{{{math.group(3)}}}{math.group(4)}"')
        else:
            break
            
    code_content = re.sub(r'如果\s*:(.*?)(>=|<=|>|<)(.*)', r'if float(\1) \2 float(\3):', code_content)
    code_content = re.sub(r'如果\s*:(.*?)==(.*)', r'if str("\1") == str("\2"):', code_content)
    # 替换变量
    while True:
        math = re.search(r'(f?)"(.*?)%\$(.*?)\$%(.*?)"', code_content)
        if math:
            code_content = code_content.replace(f'{math.group(1)}"{math.group(2)}%${math.group(3)}$%{math.group(4)}"', f'f"{math.group(2)}{{{math.group(3)}}}{math.group(4)}"')
        else:
            break
    code_content = re.sub(r'%\$(.*?)\$%', r'\1', code_content)
    code_content = re.sub(r'\n(\s*)否则\n', r'\n\1else:\n', code_content)
        
    print(file_path_new)
    # 写入文件
    with open(file_path_new, "w") as write_file:
        write_file.write(code_content)
        
    exec(f"from 中文代码.Code import {file_name.replace('.py', '')}")

if __name__ == "__main__":
    print("请不要直接运行该文件")