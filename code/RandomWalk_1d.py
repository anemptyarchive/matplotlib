
# 1次元ランダムウォークの作図

# %%

# 利用するライブラリ
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# %%

### 乱数の生成

# 試行回数を指定
max_iter = 100

# サンプルサイズを指定
sample_size = 12

# 乱数を生成
random_arr = np.random.choice([-1, 1], size=(sample_size, max_iter), replace=True)

# 試行ごとに集計
y_arr = np.cumsum(
    np.hstack([np.zeros(shape=(sample_size, 1)), random_arr]), # 初期値を追加
    axis=1
)

# %%

### グラフの作成

# グラフサイズを設定
axis_size = np.abs(y_arr).max() + 1

# 1次元ランダムウォークを作図
fig, ax = plt.subplots(figsize=(12, 9), dpi=100, facecolor='white')
ax.axhline(y=0, color='red', linestyle='dashed') # 初期値
for s in range(sample_size):
    ax.plot(np.arange(max_iter+1), y_arr[s], alpha=0.3) # 軌跡
    ax.scatter(x=max_iter, y=y_arr[s, max_iter], s=100) # 最終地点
ax.set_xlabel('iteration')
ax.set_ylabel('y')
ax.set_title('iteration: '+str(max_iter), loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.set_ylim(ymin=-axis_size, ymax=axis_size)
ax.grid()

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/1d_n.png')

plt.show()

# %%

### アニメーションの作成

# 余白サイズを指定
margin_rate = 0.1

# グラフサイズを設定
axis_size = np.ceil(
    np.abs(y_arr).max() * (margin_rate + 1)
)

# グラフオブジェクトを初期化
fig, ax = plt.subplots(figsize=(12, 9), dpi=100, facecolor='white')
fig.suptitle('Random Walk', fontsize=20)

# 作図処理を定義
def update(i):
    
    # 前フレームのグラフを初期化
    plt.cla()

    # 1次元ランダムウォークを作図
    ax.axhline(y=0, color='red', linestyle='dashed') # 初期値
    for s in range(sample_size):
          ax.plot(np.arange(i+1), y_arr[s, :i+1], alpha=0.3) # 軌跡
          ax.scatter(x=i, y=y_arr[s, i], s=100) # 現在地点
    ax.set_xlabel('iteration')
    ax.set_ylabel('y')
    ax.set_title('iteration: '+str(i), loc='left')
    ax.set_xlim(xmin=-margin_rate*max_iter, xmax=(margin_rate+1)*max_iter)
    ax.set_ylim(ymin=-axis_size, ymax=axis_size)
    ax.grid()

# 動画を作成
ani = FuncAnimation(fig=fig, func=update, frames=max_iter+1, interval=100)

# 動画を書出
ani.save(filename='../figure/RandomWalk/1d_n.mp4')


# %%


