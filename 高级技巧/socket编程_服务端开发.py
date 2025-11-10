import socket
# 创建socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(('localhost',8888))
# 监听端口
socket_server.listen(1)
# listen方法内接受一个整数传参数，表示接受的链接数量
# 等待客户端链接
# result = socket_server.accept()
# conn = result[0]    # 客户端和服务段的链接对象
# addr = result[1]    # 客户端的地址信息
conn, addr = socket_server.accept()
# accept方法返回的是二元元组（链接对象，客户端地址信息）
print(f"接受到了客户端的链接，客户端的信息是{addr}")
while True:
    # 接收客户端信息，要使用客户端和服务端的本次连接对象，而非socket——server
    data = conn.recv(1024).decode("utf-8")
    print(f"客户端发来的消息是：{data}")
    # 输入回复消息
    msg = input("请输入你要和客户端回复的消息")
    if msg == "exit":
        break
    conn.send(msg.encode("utf-8"))
# 关闭连接
conn.close()
socket_server.close()