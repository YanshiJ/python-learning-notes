read = open("F:/image.txt","r",encoding = "utf-8")
write = open("F:/bill.txt","w",encoding = "utf-8")
for line in read:
    if line.count("测试")>0:
        continue
    else:
        write.write(line)
read.close()
write.close()



read.close()