# -*- coding: UTF-8 -*-

# exit 用于中断程序，令游戏结束
from sys import exit

def gold_room():
    print "How much gold do you take?"
    next = raw_input('>')

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("HAHA")

    if how_much < 50:   # 如果这里写45，会四舍五入为50
        print "Win!"
        exit(0)   # 游戏结束	
    else:
        dead("HAHA")

def dead(why):
    print why, "GG!"
    exit(0)  # 游戏结束
	
def start():
    next = raw_input("left or right? \n>")
	
    if next == "left":
        bear_room()
    elif next == "right":
        gold_room()
    else:
        dead("HAHA")

def bear_room():
    bear_moved = False

	# 这个无限循环挺巧妙的，表示要两步才行，先让熊走开，再开门
    while True:
        next = raw_input("There is a bear here, take honey or taunt bear or open door? \n>")
        
        if next == "take honey":
            dead("HAHA")
        elif next == "taunt bear" and not bear_moved:
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("HA")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("Continue")

start()