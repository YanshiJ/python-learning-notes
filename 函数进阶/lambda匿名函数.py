def test_func(add):
    result = add(1,2)
    print(result)
test_func(lambda x,y:x+y)
test_func(lambda x,y:x**y)
# 临时构建函数