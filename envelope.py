import numpy as np
import pylab as pl      #Pythonにおいて数値計算を効率的に行うための拡張モジュール
def f(x,t):             #包絡線のもとの関数を定義
   return t * x - t**2

u = 0.5  　　　#後に非正数値刻みにするために予め定義しておく

def subplots():
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    
    return fig, ax


fig, ax = subplots()  # Call the local version, not plt.subplots()
x = np.linspace(-15, 15, 100)　#xの範囲設定
plt.xlim([x.min(),x.max()])  #y軸の範囲
plt.ylim([-30,40])　　　　
ax.set_xticks([])　　　　#x,y軸の目盛消し
ax.set_yticks([]) 
fig.suptitle('Envelope Theorem', fontsize=15)
for  n in range(-10, 11):　　　　　#-10~10の範囲でまわす
    y = f(x,t = n * u)　　　　　　　#u=0.5よりtは0.5刻みになる
    ax.plot(x, y, 'r-', linewidth=1.0, label='sine function', alpha=0.6)
    

plt.show()








