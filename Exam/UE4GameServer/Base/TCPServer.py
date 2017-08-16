from socket import *
from time import sleep
import os

host = '127.0.0.1'
port = 9999
bufsize = 1024
addr = (host,port)

#定义函数，回发信息给客户端
def handle_client(client_socket):
    #打印客户端发送的消息
    request = client_socket.recv(1024)
    print("[*] Received: %s" % request)
    #返回一个数据包，内容为ACK!
    client_socket.send('ACK!')
    client_socket.close()

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(addr)
tcpServer.listen(5) #这里设置监听数为5(默认值),有点类似多线程。

while True:
    #sleep(0.1)
    print('Waiting for connection...')
    tcpClient,addr = tcpServer.accept() #拿到5个中一个监听的tcp对象和地址
    print('[+]...connected from:',addr)

    while True:
        bytebuff = tcpClient.recv(bufsize);
        if not bytebuff:
            break
        cmd = bytebuff.decode(encoding="utf-8")
        print('   [-]cmd:',cmd)
        ###这里在cmd中执行来自客户端的命令，并且将结果返回###
        cmdResult = cmd;
        #################################################
        data = cmdResult;
        tcpClient.send(data.encode(encoding="utf-8"))

    tcpClient.close();
    print(addr,'End');
tcpServer.close() #两次关闭，第一次是tcp对象，第二次是tcp服务器