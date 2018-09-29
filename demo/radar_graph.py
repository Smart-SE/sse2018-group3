
#!/usr/bin/env python
#モジュールインポート
   
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from matplotlib.projections.polar import PolarAxes as pa
from matplotlib.projections import register_projection as rp
from pylab import *
from PIL import Image

# グラフテンプレート作成
class RadarAxes(PolarAxes):
    """Class for creating a radar chart (a.k.a. a spider or star chart)        
    http://en.wikipedia.org/wiki/Radar_chart
    """
    name = 'radar'
    # use 1 line segment to connect specified points
    RESOLUTION = 1

    def draw_frame(self, x0, y0, r):
        verts = [(r*cos(t) + x0, r*sin(t) + y0) for t in theta]
        return Polygon(verts, closed=True)

    def set_varlabels(self, theta, labels):
        self.set_thetagrids(theta * 180/pi, labels)

    def get_axes_patch(self):
        x0, y0 = (0.5, 0.5)
        r = 0.5
        return self.draw_frame(x0, y0, r)
    

def create_radar_graph(var):

    # 色変え設定
    if var >= 180 : color = 'r'
    elif var >= 120 : color = 'orange'
    elif var < 120 : color = 'g'

    rp(RadarAxes)
    
  # 要素数
    N = 4
  # 図表の傾き
    theta = 2*pi * linspace(0, 1, N+1)[:-1]
    theta += pi/2
  # ラベル
    labels = ['Anger', 'Joy', 'Hapiness', 'Sad']
  # MAX値（分母）
    rule_of_four = [255, 100, 100, 100]
  # 測定値
    desc = [var, 45, 60, 50]   #  ←！！！！ここの一番左に測定値を代入！！！！
    
  # グラフ描写
    fig = plt.figure(figsize=(2.4,2.2)) # サイズ設定
    fig.subplots_adjust(bottom=0.16) #余白設定
    desc_rate = [100*desc[i]/float(v) for (i,v) in enumerate(rule_of_four)]
    ax = subplot(111, projection='radar')
    # ax.plot(theta, desc_rate, color='black') # 輪郭
    ax.fill(theta, desc_rate, facecolor=color)
    
    for patch in ax.patches:
        patch.set_alpha(0.5)

  # ％ラベル刻み設定
    ax.set_varlabels(theta,labels)
    rgrids((50,100))

    grid(True)
    
  # png保存
    plt.savefig('rc_graph.png') 
 
  # jpeg変換
    img = Image.open('rc_graph.png')
    rgb_im = img.convert('RGB')
    rgb_im.save('rc_graph.jpg','JPEG')
    
    plt.close()
    
    
    
#var1 = 100
#create_radar_graph(var1)
