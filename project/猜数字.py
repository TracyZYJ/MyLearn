#!/usr/bin/python
# -*- coding: utf-8 -*-

print("---------test1--------")
temp = input("猜猜我最喜欢的数字：")
guess = int(temp)
if guess == 6:
     print("神算子啊你！")
     print("哈哈，那也没有奖励")
else:
    print("不对不对，哎，再猜一次吧:")
    two = input("猜猜我最喜欢的数字：")
    guess = int(two)
    if guess == 6:
        print("可算是猜对了，我们还是好朋友")
    else:
        print ("天啊噜，是6啊，拜拜了您嘞~~~")
print("溜了，不玩了")
