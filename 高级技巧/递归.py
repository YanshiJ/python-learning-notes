import os
def test_os():
    print(os.listdir("F:/test"))
    print(os.path.isdir("F:/test/a")) # 判断是否为文件夹
    print(os.path.exists("F:/test"))    # 判断路径是否存在

def get_file_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式获取全部的文件列表
    :param path:被判断的文件夹
    :return:list，包含全部文件，如果目录不存在或者无文件，就返回一个空list
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                # 进入这里表明目录是文件夹不是文件
                file_list += get_file_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"您所传入路径{path}，不存在")
        return []

    return file_list




if __name__ == '__main__':
    get_file_recursion_from_dir("F:/test")
    print(get_file_recursion_from_dir("F:/test"))