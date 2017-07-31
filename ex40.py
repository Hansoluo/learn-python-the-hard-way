# -*- coding: UTF-8 -*-

class Song(object):

    def __init__(self, lyrics):  # 初始化
        self.lyrics = lyrics
		
    def sing_me_a_song(self):    # 函数，打印歌词
        for line in self.lyrics:
            print line

    def split_a_song(self):
        word = self.lyrics.split(" ")
        print word

# 实例化一个类再赋给变量
happy_bday = Song(["happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
				   
bulls_on_parade = Song(["There rally around the family",
                         "with pockets full of shells"])

a_song = Song("There ia a crack in everything")

# 调用类
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# 附加练习
a_song.split_a_song()


