# 基础数据类型注解
import json
import random

var_1: int = 10
var_2: str = "hello"
var_3: bool = True
# 类对象类型注解
class student():
    pass
stu : student = student()
# 基础容器类型注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int,str,bool] = (1, "hello", True)
my_dict: dict[str,int] = {"name": 1213}
# 在注释中进行类型注解
var1 = random.randint(1,10)     # type:int
var2 = json.loads('{"name":"james "}')  # type: dict[str,str]
def func1():
    return 10
var3 = func1() # type: int
# 类型注解是提示性的，类似备注，不会真正的对类型进行验证和判断