def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,"r",encoding="utf-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(f"文件不存在，异常，原因是{e}")
    finally:
        if f:      # 如果变量是None，表示False，如果有任何内容就是Ture
            f.close()

def append_file_info(file_name):
    f = open(file_name,"a",encoding="utf-8")
    f.write(input("输入您想追加的内容"))
    f.close()

if __name__ == '__main__':
    append_file_info("F://bill.txt")