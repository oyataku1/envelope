
import matplotlib.pyplot as plt
import numpy as np  #Pythonにおいて数値計算を効率的に行うための拡張モジュール
def f(x,t):     
   return t * x - t**2 #包絡線のもとの関数を定義

u = 0.1  #後に非正数値刻みにするために予め定義しておく

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
x = np.linspace(-1, 1, 200)　#xの範囲設定
plt.xlim([x.min(),x.max()]) #x軸の範囲
plt.ylim([-100,200])        #y軸の範囲
ax.set_xticks([]) #x,y軸の目盛消し
ax.set_yticks([]) 
for  n in range(-10, 11):　　#-10~10の範囲でまわす
    y = f(x,t = n * u)      #u=0.1よりtは0.1刻みになる
    ax.plot(x, y, 'r-', linewidth=2, label='sine function', alpha=0.6)

plt.show()







