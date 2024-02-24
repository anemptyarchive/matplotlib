
# 1次元ランダムウォークの作図

# %%

# 利用するライブラリ
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# %%

### 乱数の生成

# 試行回数を指定
max_iter = 600

# サンプルサイズを指定
sample_size = 10

# 乱数を生成
random_arr = np.random.choice([-1, 1], size=(sample_size, max_iter), replace=True) # 移動量

# 試行ごとに集計
x_arr = np.cumsum(
    np.hstack([np.zeros(shape=(sample_size, 1)), random_arr]), # 初期値を追加
    axis=1
)

# %%

### グラフの作成：(サンプル軸あり)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.abs(x_arr).max()
axis_size = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# 1Dランダムウォークを作図
fig, ax = plt.subplots(figsize=(9, 6), facecolor='white')
ax.axhline(y=0, color='red', linestyle='dashed') # 初期値
for s in range(sample_size):
    ax.plot(np.repeat(s+1, repeats=max_iter+1), x_arr[s]) # 軌跡
    ax.scatter(x=s+1, y=x_arr[s, max_iter], s=100, zorder=10) # 最終地点
ax.set_xlabel('sample')
ax.set_ylabel('x')
ax.set_title('iteration: '+str(max_iter), loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.set_ylim(ymin=-axis_size, ymax=axis_size)
ax.grid()

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/1d_x_n.png', dpi=250)

plt.show()

# %%

### アニメーションの作成：(サンプル軸あり)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.abs(x_arr).max()
axis_size = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# グラフオブジェクトを初期化
fig, ax = plt.subplots(figsize=(9, 6), facecolor='white')
fig.suptitle('Random Walk', fontsize=20)

# 作図処理を定義
def update(i):
    
    # 前フレームのグラフを初期化
    plt.cla()

    # 1Dランダムウォークを作図
    ax.axhline(y=0, color='red', linestyle='dashed') # 初期値
    for s in range(sample_size):
        ax.plot(np.repeat(s+1, repeats=i+1), x_arr[s, :i+1]) # 軌跡
        ax.scatter(x=s+1, y=x_arr[s, i], s=100, zorder=10) # 現在地点
    ax.set_xlabel('sample')
    ax.set_ylabel('x')
    ax.set_title('iteration: '+str(i), loc='left')
    ax.set_ylim(ymin=-axis_size, ymax=axis_size)
    ax.grid()

# 動画を作成
ani = FuncAnimation(fig=fig, func=update, frames=max_iter+1, interval=100)

# 動画を書出
ani.save(
    filename='../figure/RandomWalk/1d_x_n.mp4', dpi=250, 
    progress_callback = lambda i, n: print(f'frame: {i} / {n}')
)

# %%

### グラフの作成：(時間軸あり)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.abs(x_arr).max()
axis_size = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# 1Dランダムウォークを作図
fig, ax = plt.subplots(figsize=(12, 9), facecolor='white')
ax.axhline(y=0, color='red', linestyle='dashed') # 初期値
ax.plot(np.arange(max_iter+1), x_arr.T, alpha=0.4) # 軌跡
for s in range(sample_size):
    ax.scatter(x=max_iter, y=x_arr[s, max_iter], s=100, zorder=10) # 最終地点
ax.set_xlabel('iteration')
ax.set_ylabel('x')
ax.set_title('iteration: '+str(max_iter), loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.set_ylim(ymin=-axis_size, ymax=axis_size)
ax.grid()

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/1d_ix_n.png', dpi=250)

plt.show()

# %%

### アニメーションの作成：(時間軸あり)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.abs(x_arr).max()
axis_size = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# グラフオブジェクトを初期化
fig, ax = plt.subplots(figsize=(12, 9), facecolor='white')
fig.suptitle('Random Walk', fontsize=20)

# 作図処理を定義
def update(i):
    
    # 前フレームのグラフを初期化
    plt.cla()

    # 1Dランダムウォークを作図
    ax.axhline(y=0, color='red', linestyle='dashed') # 初期値
    ax.plot(np.arange(i+1), x_arr.T[:i+1], alpha=0.4) # 軌跡
    for s in range(sample_size):
        ax.scatter(x=i, y=x_arr[s, i], s=100, zorder=10) # 現在地点
    ax.set_xlabel('iteration')
    ax.set_ylabel('x')
    ax.set_title('iteration: '+str(i), loc='left')
    ax.set_xlim(xmin=-max_iter*margin_rate, xmax=max_iter*(1+margin_rate))
    ax.set_ylim(ymin=-axis_size, ymax=axis_size)
    ax.grid()

# 動画を作成
ani = FuncAnimation(fig=fig, func=update, frames=max_iter+1, interval=100)

# 動画を書出
ani.save(
    filename='../figure/RandomWalk/1d_ix_n.mp4', dpi=250, 
    progress_callback = lambda i, n: print(f'frame: {i} / {n}')
)

# %%


