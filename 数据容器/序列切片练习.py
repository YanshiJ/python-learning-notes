str = "万过薪月，员序程马黑来，nohtyP学"
reverse = str[::-1]
print(reverse)
new_str = reverse.split("，")
print(new_str[1])
another_str = new_str[1]
print(another_str)
result = another_str[1: ]
print(result)

