
# 1次元ランダムウォークの作図

# %%

# ライブラリを読込
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# %%

### 乱数の生成 ------------------------------------------------------------------

# サンプルサイズを指定
sample_size = 10

# 試行回数を指定
max_iter = 600

# 乱数を生成
random_arr = np.random.choice([-1, 1], size=(sample_size, max_iter), replace=True) # 移動量

# 試行ごとに集計
x_arr = np.cumsum(
    np.hstack([np.zeros(shape=(sample_size, 1)), random_arr]), # 初期値を追加
    axis=1
)


# %%

### グラフの作成：(サンプル軸付き) ------------------------------------------------

# グラフサイズを設定
margin_rate  = 0.1
axis_val_max = np.ceil(np.abs(x_arr).max() * (1.0+margin_rate))
axis_val_min = -axis_val_max

# 1Dランダムウォークを作図
fig, ax = plt.subplots(figsize=(8, 6), dpi=100, facecolor='white', constrained_layout=True)
ax.axhline(y=0.0, color='black', linestyle='dashed') # 初期値
for i in range(sample_size):
    ax.plot(np.tile(i+1, reps=max_iter+1), x_arr[i], alpha=0.5) # 推移
    ax.scatter(x=i+1, y=x_arr[i, max_iter]) # 最終値
ax.set_xlabel('sample')
ax.set_ylabel('value')
ax.set_title(f'sample size: {sample_size}, iteration: {max_iter}', loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.grid()
ax.set_ylim(ymin=axis_val_min, ymax=axis_val_max)

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/1d_value_sample.png')

plt.show()


# %%

### グラフの作成：(時間軸付き) ---------------------------------------------------

# グラフサイズを設定
margin_rate  = 0.1
axis_val_max = np.ceil(np.abs(x_arr).max() * (1.0+margin_rate))
axis_val_min = -axis_val_max

# 1Dランダムウォークを作図
fig, ax = plt.subplots(figsize=(8, 6), dpi=100, facecolor='white', constrained_layout=True)
ax.axhline(y=0.0, color='black', linestyle='dashed') # 初期値
for i in range(sample_size):
    ax.plot(np.arange(max_iter+1), x_arr[i], alpha=0.5) # 推移
    ax.scatter(x=max_iter, y=x_arr[i, max_iter]) # 最終値
ax.set_xlabel('iteration')
ax.set_ylabel('value')
ax.set_title(f'sample size: {sample_size}, iteration: {max_iter}', loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.set_ylim(ymin=axis_val_min, ymax=axis_val_max)
ax.grid()

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/1d_value_iteration.png')

plt.show()


# %%

### アニメーションの作成：(時間軸・サンプル軸付き) ---------------------------------

# 配色の共通化用のカラーマップを作成
cmap = plt.get_cmap('tab10')
color_num = 10 # カラーマップごとに固定

# グラフサイズを設定
margin_rate   = 0.1
axis_iter_min = -max_iter * margin_rate
axis_iter_max = max_iter * (1.0+margin_rate)
axis_val_max  = np.ceil(np.abs(x_arr).max() * (1.0+margin_rate))
axis_val_min  = -axis_val_max

# グラフオブジェクトを初期化
fig, axes = plt.subplots(nrows=1, ncols=2, 
                         figsize=(10, 6), width_ratios=[4, 1], 
                         dpi=100, facecolor='white', constrained_layout=True)
fig.suptitle('Random Walk', fontsize=20)

# 作図処理を定義
def update(t):
    
    # 前フレームのグラフを初期化
    [ax.cla() for ax in axes]

    # 1Dランダムウォークを描画:時間軸
    ax = axes[0]
    ax.axhline(y=0.0, color='black', linestyle='dashed') # 初期値
    for i in range(sample_size):
        tmp_color = cmap(i%color_num)
        ax.hlines(y=x_arr[i, t], xmin=t, xmax=axis_iter_max, 
                  color=tmp_color, linestyles='dotted') # 目盛線
        ax.plot(np.arange(t+1), x_arr[i, :(t+1)], 
                color=tmp_color, alpha=0.5, linewidth=1.0) # 推移
        ax.scatter(x=t, y=x_arr[i, t], 
                   color=tmp_color, s=50, zorder=10) # 現在値
    ax.set_xlabel('iteration')
    ax.set_ylabel('value')
    ax.set_title(f'sample: {sample_size}, iteration: {t}', loc='left')
    ax.grid()
    ax.set_xlim(xmin=axis_iter_min, xmax=axis_iter_max)
    ax.set_ylim(ymin=axis_val_min, ymax=axis_val_max)

    # 1Dランダムウォークを描画:サンプル軸
    ax = axes[1]
    ax.axhline(y=0.0, color='black', linestyle='dashed') # 初期値
    for i in range(sample_size):
        tmp_color = cmap(i%color_num)
        ax.hlines(y=x_arr[i, t], xmin=0, xmax=i+1, 
                  color=tmp_color, linestyles='dotted') # 目盛線
        ax.plot(np.tile(i+1, reps=t+1), x_arr[i, :(t+1)], 
                color=tmp_color, alpha=0.5, linewidth=1.0) # 推移
        ax.scatter(x=i+1, y=x_arr[i, t], 
                   color=tmp_color, s=50, zorder=10) # 現在値
    ax.set_xlabel('sample')
    ax.set_ylabel('value')
    ax.grid()
    ax.set_xlim(xmin=0, xmax=sample_size+1)
    ax.set_ylim(ymin=axis_val_min, ymax=axis_val_max)

# 動画を作成
ani = FuncAnimation(fig=fig, func=update, frames=max_iter+1, interval=100)

# 動画を書出
ani.save(
    filename='../figure/RandomWalk/1d_value_iteration_sample.mp4', 
    progress_callback = lambda i, n: print(f'frame: {i} / {n}')
)


# %%

### アニメーションの作成：(時間軸・度数軸付き) -------------------------------------

# グラフサイズを設定
margin_rate   = 0.1
axis_iter_min = -max_iter * margin_rate
axis_iter_max = max_iter * (1.0+margin_rate)
axis_val_max  = np.ceil(np.abs(x_arr).max() * (1.0+margin_rate))
axis_val_min  = -axis_val_max
axis_cnt_min  = -sample_size * margin_rate
axis_cnt_max  = sample_size * 0.5 # (0.5は表示範囲の調整用)

# グラフオブジェクトを初期化
fig, axes = plt.subplots(nrows=1, ncols=2, 
                         figsize=(10, 6), width_ratios=[4, 1], 
                         dpi=100, facecolor='white', constrained_layout=True)
fig.suptitle('Random Walk', fontsize=20)

# 作図処理を定義
def update(t):
    
    # 前フレームのグラフを初期化
    [ax.cla() for ax in axes]

    # 1Dランダムウォークを描画:時間軸あり
    ax = axes[0]
    ax.axhline(y=0.0, color='black', linestyle='dashed') # 初期値
    ax.plot(np.arange(t+1), x_arr.T[:(t+1)], 
            color='C0', alpha=0.1, linewidth=1.0) # 推移
    ax.scatter(x=np.tile(t, reps=sample_size), y=x_arr[:, t], 
               color='C0', s=5) # 現在値
    ax.set_xlabel('iteration')
    ax.set_ylabel('value')
    ax.set_title(f'sample: {sample_size}, iteration: {t}', loc='left')
    ax.grid()
    ax.set_xlim(xmin=axis_iter_min, xmax=axis_iter_max)
    ax.set_ylim(ymin=axis_val_min, ymax=axis_val_max)

    # 1Dランダムウォークを描画:サンプル軸あり
    ax = axes[1]
    ax.axhline(y=0.0, color='black', linestyle='dashed') # 初期値
    ax.hist(x_arr[:, t], color='C0', orientation='horizontal') # 度数
    ax.scatter(x=np.tile(0.5*axis_cnt_min, reps=sample_size), y=x_arr[:, t], # (0.5は表示位置の調整用)
               color='C0', alpha=0.1, s=5) # 現在値
    ax.set_xlabel('count')
    ax.set_ylabel('value')
    ax.grid()
    ax.set_xlim(xmin=axis_cnt_min, xmax=axis_cnt_max)
    ax.set_ylim(ymin=axis_val_min, ymax=axis_val_max)

# 動画を作成
ani = FuncAnimation(fig=fig, func=update, frames=max_iter+1, interval=100)

# 動画を書出
ani.save(
    filename='../figure/RandomWalk/1d_value_iteration_count.mp4', 
    progress_callback = lambda i, n: print(f'frame: {i} / {n}')
)


 # %%


