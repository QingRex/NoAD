import os

def replace_and_save(file_path, current_script):
    # 如果当前文件是脚本本身，跳过
    if file_path == current_script:
        return

    # 打开文件并读取内容
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 仅替换 'RuCu6/Loon' 为 'QingRex/NoAD'
        content = content.replace('RuCu6/Loon', 'QingRex/NoAD')

        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf8') as file:
            file.write(content)

        print(f"文件处理完成: {file_path}")
    except Exception as e:
        print(f"处理文件 {file_path} 时发生错误: {e}")

def process_directory(directory):
    # 获取当前脚本的文件名
    current_script = os.path.basename(__file__)

    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # 跳过当前脚本文件
            if file != current_script:
                replace_and_save(file_path, current_script)

# 指定要处理的目录
directory = '.'  # 当前目录，也可以替换为其他目录路径
process_directory(directory)
