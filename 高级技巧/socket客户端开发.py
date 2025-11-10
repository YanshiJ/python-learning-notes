import socket
# 创建socket对象
socket_client = socket.socket()
# 连接到服务端
socket_client.connect(("127.0.0.1",8888))
while True:
    # 发送消息
    msg = input("输入您想发送的消息：")
    socket_client.send(msg.encode("utf-8"))
    if msg == "exit":
        break
    # 接受返回消息
    recv_data = socket_client.recv(1024).decode("utf-8")
    print(f"服务端回复的消息是{recv_data}")
socket_client.close()