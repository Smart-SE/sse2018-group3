#!/usr/bin/env python
# -*- coding: utf-8 -*- 


def check(pulse, lst):
    if pulse == 0:
        lst[0] = "緊急事態！ マジ危険な状態です。 "
        lst[1] = "shinpaku_1.jpeg"
    elif pulse <= 50:
        lst[0] = "体調をしんぱい してくだい！ 怒ってないけど、体調が悪いかも。"
        lst[1] = "shinpaku_2.jpeg"
    elif pulse <= 90:
        lst[0] = "あんしん してください！ 機嫌がよさそうです。穏やかな生活を楽しめそうです。"
        lst[1] = "shinpaku_3.jpeg"
    elif pulse <= 120:
        lst[0] = "ちゅうい してください！ 若干イライラしているようです。 言葉遣いには気を付けましょう。"
        lst[1] = "shinpaku_4.jpeg"
    elif pulse <= 180:
        lst[0] = "けいかい してください！ かなり危険な状態です。 美味しいお土産を買ってかえりましょう。" 
        lst[1] = "shinpaku_5.jpeg"
    else:
        lst[0] = "大噴火 しています！ 触らぬ神に祟りなし。 そっとしておきましょう。"
        lst[1] = "shinpaku_6.jpeg"

"""
str_list = ["",""]
check(0, str_list)
print(str_list)
check(50, str_list)
print(str_list)
check(90, str_list)
print(str_list)
check(120, str_list)
print(str_list)
check(180, str_list)
print(str_list)
check(181, str_list)
print(str_list)
"""