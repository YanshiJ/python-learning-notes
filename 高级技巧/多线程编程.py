import time
import threading

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)
def dance(msg):
    while True:
        print(msg)
        time.sleep(1)
if __name__ == '__main__':
    # 创建唱歌线程
    thread1 = threading.Thread(target=sing,args=("唱歌好啊", ))
    # 创建跳舞线程
    thread2 = threading.Thread(target=dance,kwargs={"msg":"我在跳舞呢"})
    thread1.start()
    thread2.start()