
# coding: utf-8

#import module
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image


def create_line_graph(var_list):
    # figure
    fig = plt.figure(figsize=(2.4,2.2)) #サイズ設定
    fig.subplots_adjust(bottom=0.16, left=0.30) #余白設定

    # graph
    ax = fig.add_subplot(1,1,1) #グラフ作成
    ax.set_xlabel("Time") #xラベル
    ax.set_ylabel("Angerlevel") #yラベル
    ax.set_title('TimeSeriesGraph') #グラフタイトル
    ax.xaxis.set_major_formatter(plt.NullFormatter()) #x軸の値を非表示
    ax.plot(var_list)

    # save as png
    plt.savefig('line_graph.png')
            
    # Convert jpeg
    im = Image.open('line_graph.png')
    rgb_im = im.convert('RGB')
    rgb_im.save('line_graph.jpg','JPEG')
            
    plt.close()


#variable
x = [100,52,33,44,55,16,47,38,39,100]
create_line_graph(x)
