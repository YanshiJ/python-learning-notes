members_info = {"王力宏":{
    "apartment" : "tech",
    "salary" : 3000,
    "level" : 1
}, "周杰伦":{
    "apartment" : "marketing",
    "salary": 5000,
    "level" : 2
},"林俊杰":{
    "apartment" : "marketing",
    "salary": 7000,
    "level": 3
},"张学友":{
    "apartment" : "tech",
    "salary": 4000,
    "level": 1
},"刘德华":{
    "apartment" : "tech",
    "salary": 6000,
    "level": 2
}}
print(f"全体员工当前信息如下：{members_info}")
for members in members_info:
    if members_info[members]["level"] == 1:
        members_info[members]["level"] += 1
        members_info[members]["salary"] += 1000
    else:
        continue
print(f"全体员工完成升职加薪后：{members_info}")