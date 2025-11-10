i = 1
total = 10000
per_person = 1000
for i in range (1,21):
    import random
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i}绩点不达标哦，为{num}，领不到工资呢")
        continue
    else:
        total = total - per_person
        print(f"员工{i}绩点达标，为{num}，获得工资{per_person}元")
        if total == 0:
            break
print(f"工资发完啦，当前余额{total},下个月再来吧")