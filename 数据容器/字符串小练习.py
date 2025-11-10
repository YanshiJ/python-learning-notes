words = "itheima itcast boxuegu"
it_num = words.count("it")
print(f"字符串{words}中有：{it_num}个it字符")
new_words = words.replace(" ","|")
print(new_words)
words_list = new_words.split("|")
print(words_list)