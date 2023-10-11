import os
import platform
import argparse
from FileInfoUtils import FileInfo
from FileHashCalculatorUtils import FileHashCalculator

file_path = None
file_list = []
hash_algorithm = 'sha256'


# 初始化
def init():
    global file_path, hash_algorithm
    parser = argparse.ArgumentParser(description="处理路径参数")
    # 添加参数
    parser.add_argument("--path", type=str, help="文件夹路径")
    parser.add_argument("--hash", type=str, help='哈希算法，可选值为 "md5", "sha256", "sha512"，默认为 "sha256"')
    args = parser.parse_args()
    # 获取命令行参数的值
    if args.path and args.hash:
        file_path = args.path
        hash_algorithm = args.hash
        welcome()
        file_traversal()
    else:
        welcome()
        print("You did not provide a folder path, start the example (sd.exe --path C:/Users/Administrator/1 --hash sha256)")
        print("Pressing any key will close the program.")
        input()
        exit()

# 清理控制台
def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# 欢迎界面
def welcome():
    clear_terminal()
    print(r"""
  _________.__        .__.__               .__  __           ________          __                 __                
 /   _____/|__| _____ |__|  | _____ _______|__|/  |_ ___.__. \______ \   _____/  |_  ____   _____/  |_  ___________ 
 \_____  \ |  |/     \|  |  | \__  \\_  __ \  \   __<   |  |  |    |  \_/ __ \   __\/ __ \_/ ___\   __\/  _ \_  __ \
 /        \|  |  Y Y  \  |  |__/ __ \|  | \/  ||  |  \___  |  |    `   \  ___/|  | \  ___/\  \___|  | (  <_> )  | \/
/_______  /|__|__|_|  /__|____(____  /__|  |__||__|  / ____| /_______  /\___  >__|  \___  >\___  >__|  \____/|__|   
        \/          \/             \/                \/              \/     \/          \/     \/                   
          """)
    print("Author: Ryan Zhang(https://github.com/hz157)".rjust(100))
    print("Version: v23.10.1117".rjust(100))

def file_traversal():
    global file_path, file_list
    for root, dirs, files in os.walk(file_path):
        count = 1
        for file in files:
            sub_path = os.path.join(root, file)
            file_info = cache_file_info(sub_path)
            print(f'Processing {sub_path}')
            file_list.append(file_info)
            count = count + 1
    print(f"Total {len(file_list)} files in {file_path} folder.")
    print_menu()

def print_menu():
    print("""
    1. 打印文件列表
    2. 打印相同哈希文件
    3. 退出
    """)
    user_input = input("请输入序号：")
    if user_input == "1":
        print_file_list()
    elif user_input == "2":
        print_same_hash_file()
    elif user_input == "3":
        exit()

def print_file_list():
    for file_info in file_list:
        for item in file_info:
            print(f'{item}: {file_info[item]}')
        print(' ')

def print_same_hash_file():
    clear_terminal()
    hash_to_filenames = {}

    # 遍历文件列表
    for file_info in file_list:
        file_name = file_info['File_Name']
        file_hash = file_info['File_Hash']

        # 如果哈希值已经存在于字典中，将文件名添加到对应的列表中
        if file_hash in hash_to_filenames:
            hash_to_filenames[file_hash].append(file_name)
        else:
            # 否则，创建一个新的列表并将文件名添加到列表中
            hash_to_filenames[file_hash] = [file_name]

    # 打印出具有相同哈希值的文件名
    for hash_value, filenames in hash_to_filenames.items():
        if len(filenames) > 1:
            print(f'Match files with hash value {hash_value}({hash_algorithm}) ')
            for item in filenames:
                print(item)





def cache_file_info(file):
    file_info = FileInfo(file)
    file_dict = {"File_Name": file_info.file_name,
                "File_Path": file,
                "File_Hash": FileHashCalculator.calculate_hash(file_path=file, algorithm=hash_algorithm),
                "File_Size": f"{file_info.get_size()} bytes",
                "Create_Time": file_info.get_create_time(),
                "Modify_Time": file_info.get_modify_time(),
                "Owner": file_info.get_owner(),
                "Computer_Name": file_info.get_computer_name(),
                "File_Type": file_info.get_file_type(),
                "File_Location": file_info.get_file_location()}
    return file_dict


if __name__ == "__main__":
    init()