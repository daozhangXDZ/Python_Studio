#  -*- coding: utf-8 -*-
import aiml
import os
import sys
# init...
def alice_simple_init():
    os.chdir('./res_en/alice')  # 设定文件目录
    alice = aiml.Kernel()
    alice.learn('startup.xml')  # 选择god需要加载的xml文件
    alice.respond('LOAD GOD')  # 对应xml中的LOAD GOD模块,会加载其模块下的.aiml文件
def alice_speedup_init():
    os.chdir('./res_en/alice')  # 设定文件目录
    alice = aiml.Kernel()
    if os.path.isfile("alice.brn"):
        alice.bootstrap(brainFile="bot_brain.brn")
    else:
        alice.bootstrap(learnFiles="startup.xml", commands="LOAD alice")
        alice.saveBrain("alice.brn")
    while True:
        print(alice.respond(input("Enter your message >> ")));
if __name__ == '__main__':
    alice_speedup_init()